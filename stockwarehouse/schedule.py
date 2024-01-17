from operation.models import *
# from infotrading.models import get_all_info_stock_price
from stockwarehouse.backup import run_database_backup
from datetime import datetime
from infotrading.models import get_list_stock_price


def schedule_morning():
    today = datetime.now().date()
    not_trading_dates = DateNotTrading.objects.filter(date=today)
    # try:
    #     # Uncomment nếu bạn có một hàm check_update_analysis_and_send_notifications
    #     # check_update_analysis_and_send_notifications()
    # except Exception as e_check_update:
    #     print(f"An error occurred while running check_update_analysis_and_send_notifications: {e_check_update}")

   
    try:
        calculate_interest()
    except Exception as e_morning_check:
        print(f"An error occurred while running morning_check: {e_morning_check}")

    if not not_trading_dates:
        try:
            # Thực hiện công việc cần làm vào 7h30
            # Ví dụ: Gửi email
            # send_mail(
            #     'Morning Check',
            #     'Nội dung kiểm tra buổi sáng...',
            #     'from@example.com',
            #     ['to@example.com'],
            #     fail_silently=False,
            # )

            check_dividend_recevie()
        except Exception as e_check_dividend:
            print(f"An error occurred while running check_dividend: {e_check_dividend}")
        
        try:
            pay_money_back()
        except Exception as e_auto_news:
            print(f"An error occurred while running auto_news_stock_worlds: {e_auto_news}")
        
        try:
            run_database_backup()
        except Exception as e_auto_news:
            print(f"An error occurred while running auto_news_stock_worlds: {e_auto_news}")
    else:
        pass



def schedule_mid_trading_date():
    today = datetime.now().date()
    not_trading_dates = DateNotTrading.objects.filter(date=today)
    
    if not not_trading_dates:
        
        try:
            atternoon_check()
            
        except Exception as e_afternoon_check:
            print(f"An error occurred while running atternoon_check: {e_afternoon_check}")
        
        try:
            check_dividend_recevie()
        except Exception as e_get_info_stock:
            print(f"An error occurred while running get_info_stock_price_filter: {e_get_info_stock}")

    else:
        pass

def get_info_stock_price_filter():
    today = datetime.now().date()
    not_trading_dates = DateNotTrading.objects.filter(date=today)
    if not not_trading_dates:
        try:
            stock_list = Portfolio.objects.values_list('stock', flat=True).distinct()
            stock_list_python = list(stock_list)
            get_list_stock_price(stock_list_python)
        except Exception as e_afternoon_check:
            print(f"An error occurred while running atternoon_check: {e_afternoon_check}")
    else:
        pass


def get_info_stock_price_stock_68():
    today = datetime.now().date()
    not_trading_dates = DateNotTrading.objects.filter(date=today)
    if not not_trading_dates:
        try:
            port  = Portfolio.objects.filter(sum_stock__gt=0)
            for item in port:
                item.market_price = get_stock_market_price(item.stock)
                item.save()
                account = Account.objects.get(pk =item.account.pk)
                account.save()
        except Exception as e_afternoon_check:
            print(f"An error occurred while running atternoon_check: {e_afternoon_check}")
    else:
        pass

# def schedule_after_trading_date():
#     today = datetime.now().date()
#     not_trading_dates = DateNotTrading.objects.filter(date=today)
    
#     if not not_trading_dates:
    
#         try:
#             get_info_stock_price_filter()
#         except Exception as e_auto_news:
#             print(f"An error occurred while running auto_news_daily: {e_auto_news}")
#         # try:
#         #     filter_stock_daily()
#         # except Exception as e_filter_stock:
#         #     print(f"An error occurred while running filter_stock_daily: {e_filter_stock}")
#     else:
#         pass

