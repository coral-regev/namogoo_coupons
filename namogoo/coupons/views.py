from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from .models import Coupons, SentCoupons
import ast


@require_GET
def get_coupon(request):
    params = request.GET
    domain = params.get('domain')
    coupon_value = params.get('coupon_value')

    if domain and coupon_value:
        ''' Based on an averaged traffic calculation of Amazon.com site taken from similarweb.com,
        The situation in which more than 20 clients asks for the same domain and coupon_value in a specific request time
        is very rare, so for reasons of low latency only 20 coupons from the same domain and coupon_value
        could be sent at a given time'''
        relevant_coupons = Coupons.objects.filter(domain=domain, coupon_value=coupon_value)[:20]

        for coupon in relevant_coupons:
            coupon_code = coupon.coupon_code
            deletion_value = coupon.delete()
            # The returned deletion_value[0] will be equals one only for one client that was the first
            # to delete this coupon from the Coupons table. Others will proceed to try and get the next suitable coupon.
            if deletion_value[0] == 1:
                # We will return this coupon_code only for this client and add it to the SentCoupons value
                SentCoupons.objects.create(domain=domain, coupon_value=coupon_value, coupon_code=coupon_code)
                return JsonResponse({"coupon_code": coupon_code})

        res_message = "There is no available coupons for {} with value {}.".format(domain, coupon_value)
    else:
        res_message = "Invalid parameters"

    return JsonResponse({"message": res_message})




@require_POST
@csrf_exempt
def return_coupon(request):
    byte_params = request.body
    dict_str = byte_params.decode("UTF-8")
    params = ast.literal_eval(dict_str)
    domain = params.get('domain')
    coupon_value = params.get('coupon_value')

    if domain and coupon_value:
        coupons_list = params.get('coupons_list')
        if coupons_list:
            coupons_objects_list = []

            for coupon in coupons_list:
                # Assuming this trio is unique and will return up to one object from the filter query
                sent_coupon = SentCoupons.objects.filter(domain=domain, coupon_value=coupon_value, coupon_code=coupon)

                # Checking if the returned coupons were existed before on DB and were sent to a client
                if sent_coupon:
                    sent_coupon.delete()
                    coupons_objects_list.append(Coupons(domain=domain, coupon_value=coupon_value, coupon_code=coupon))

            Coupons.objects.bulk_create(coupons_objects_list)
        res_message = "Coupons: {} have been added successfully".format(", ".join(coupon.coupon_code for coupon in coupons_objects_list))
    else:
        res_message = "Invalid parameters"

    return JsonResponse({"message": res_message})
