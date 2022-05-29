from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
@require_POST
def coupon_apply(request):
    """
    View responsible for validating coupons
    """
    if request.session.get('coupon_id') is None:
        now = timezone.now()
        form = CouponApplyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            # if coupon is valid then apply coupon to cart session and subtract from quantity property
            try:
                coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, active=True, quantity__gt=0)
                request.session['coupon_id'] = coupon.id
                coupon.quantity -= 1
                coupon.save()
            except Coupon.DoesNotExist:
                request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
