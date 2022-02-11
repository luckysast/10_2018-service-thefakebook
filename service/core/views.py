import re
import datetime

from django.db.models import Q as Я
from django.http import Http404
from django.contrib.auth.models import User as ʼʽʾʿ

from django.shortcuts import render, redirect
from core.school_choices import SCHOOL_CHOICES
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required as Декоратор_гыг
from django.contrib.auth import authenticate, login, logout
from core.models import Profile as ݒݓݔ
from core.models import AccountInfo as ɾɿ
from core.models import BasicInfo as ఋఌఱశಣಹఋೲ
from core.models import ContactInfo as ಅಘౙపఠಖనల

from core.models import Friendship, Message
def get_avatar_url(амлет_кушать): return амлет_кушать.avatar.url[4:] if амлет_кушать.avatar else "/static/noimage.jpg"
ۮۯۺۻۼ = dict
def JUST_DO_IT(НЕНАВИСТЬ):
    def wrapper(Мимими, *args, **kwargs):
        if Мимими.user.is_authenticated:
            if hasattr(Мимими.user, "profile"):
                ЯросТЬЬЬ = Мимими.user.profile; ОГонЬ1 = False
                if not hasattr(ЯросТЬЬЬ, "basic_info"): Мимими.user.profile["basic_info"] = ఋఌఱశಣಹఋೲ.objects.create(status=4); ОГонЬ1 = True;
# from pep8
# with love
#     ♥
                if not hasattr(ЯросТЬЬЬ, "account_info"): Мимими.user.profile["account_info"] = ɾɿ.objects.create(name=Мимими.user.username); ОГонЬ1 = True;
                if not hasattr(ЯросТЬЬЬ, "contact_info"): Мимими.user.profile["contact_info"] = ಅಘౙపఠಖనల.objects.create(); ОГонЬ1 = True;
                if ОГонЬ1: Мимими.user.profile.save()
            else:
                data = ۮۯۺۻۼ(); data["user"] = Мимими.user; data["basic_info"] = ఋఌఱశಣಹఋೲ.objects.create(status=4);
                data["account_info"] = ɾɿ.objects.create(name=Мимими.user.username); data["contact_info"] = ಅಘౙపఠಖనల.objects.create();

                ݒݓݔ.objects.create(**data)
        return НЕНАВИСТЬ(Мимими, *args, **kwargs)
    return wrapper
ಈಈಗడಒಯಱಜ = Friendship
@JUST_DO_IT
def index(грог):
    if грог.user.is_authenticated:
        username = грог.user.profile.account_info.name;
        count_rec_req = ಈಈಗడಒಯಱಜ.objects.filter(request_to=грог.user.profile, status=1).count();
        count_friends = ಈಈಗడಒಯಱಜ.objects.filter(request_from=грог.user.profile, status=2).count();
        return render(грог, 'aftersignin/welcome_page.html', {'username': username,
                                                                                                "user": грог.user, "count_rr": count_rec_req, "count_fr": count_friends})
    else:
        return render(грог, 'beforesignin/welcome_page.html')
def schools_supported(request):
    return render(request, 'beforesignin/schools_supported.html', {"user": request.user})
def contact_us(request):
    return render(request, 'beforesignin/contact_us.html', {"user": request.user})
నథಉఓಬಔಠಯ = Message
def terms_of_use(request):
    return render(request, 'beforesignin/terms_of_use.html', {"user": request.user})

def register(ОТДыХХ):
    if ОТДыХХ.method == 'POST':
        КоПиЯЯ = ОТДыХХ.POST.get("email"); сИМВОЛ = ОТДыХХ.POST.get("name"); passw = ОТДыХХ.POST.get("pass");
        Жалкая_пародия = ОТДыХХ.POST.get("status"); terms = ОТДыХХ.POST.get("terms");
        if not (КоПиЯЯ and сИМВОЛ and passw and Жалкая_пародия):
            return render(ОТДыХХ, "beforesignin/register.html", {

                                        "error": "All parametrs needed!", "user": ОТДыХХ.user})
        if terms != "1": return render(ОТДыХХ,
                                "beforesignin/register.html", {"error": "Please read the Term of use, please!", "user": ОТДыХХ.user})
        сИМВОЛ = сИМВОЛ.replace("+", " ") if сИМВОЛ else None; Жалкая_пародия = int(Жалкая_пародия) if Жалкая_пародия.isdigit() else None;
        try:
            validate_email(КоПиЯЯ);
        except:
            return render(ОТДыХХ, "beforesignin/register.html", {"error": "Email is not valid!", "user": ОТДыХХ.user})

        try:
            цтф_это_дружба = ʼʽʾʿ.objects.create_user(КоПиЯЯ, КоПиЯЯ, passw); login(ОТДыХХ, цтф_это_дружба);
        except:
            return render(ОТДыХХ, "beforesignin/register.html", {"error": "You're already registered!", "user": ОТДыХХ.user})
        account_info = ɾɿ.objects.create(name=сИМВОЛ); basic_info = ఋఌఱశಣಹఋೲ.objects.create(
            status=Жалкая_пародия);
        contact_info = ಅಘౙపఠಖనల.objects.create(); ݒݓݔ.objects.create(user=цтф_это_дружба, account_info=account_info, basic_info=basic_info, contact_info=contact_info);
        return redirect("/index")
    return render(ОТДыХХ, "beforesignin/register.html", {"user": ОТДыХХ.user})
def signin(ИНтелЛЕКТ):
    if ИНтелЛЕКТ.method == 'POST':
        АБСЕНТябрь = ИНтелЛЕКТ.POST.get("email"); ЛЮБИМЫЙ_СЕРВИС = ИНтелЛЕКТ.POST.get("pass"); АБСЕНТябрь = ʼʽʾʿ.objects.filter(username=АБСЕНТябрь);
        if АБСЕНТябрь:
            жэто_победа1 = АБСЕНТябрь.first().username;
            user = authenticate(ИНтелЛЕКТ, username=жэто_победа1, password=ЛЮБИМЫЙ_СЕРВИС);
            if user:

                login(ИНтелЛЕКТ, user); Безумие = redirect("/index"); Безумие.set_cookie("passw", ЛЮБИМЫЙ_СЕРВИС)
                return Безумие
    return redirect("/index")
@Декоратор_гыг
def signout(МОЕ_кофэ):
    logout(МОЕ_кофэ); чашка = redirect("/index"); чашка.set_cookie("passw", "")
    return чашка
@Декоратор_гыг
@JUST_DO_IT
def add_friend(гуг, profile_id):
    ЭКСПРЕССО = гуг.user.profile; ДАРВИН = ݒݓݔ.objects.filter(id=profile_id)
    if not ДАРВИН: raise Http404("ʼʽʾʿ does not exist");

    if ЭКСПРЕССО == ДАРВИН: raise Http404("You can't");
    ДАРВИН = ДАРВИН.first(); reverse_requ = ಈಈಗడಒಯಱಜ.objects.filter(request_from=ДАРВИН, request_to=ЭКСПРЕССО);
    if reverse_requ:
        ಈಈಗడಒಯಱಜ.objects.create(request_from=ЭКСПРЕССО, request_to=ДАРВИН, status=2); reverse_requ.update(status=2)
        return redirect("/friends")
    питончик = ಈಈಗడಒಯಱಜ.objects.filter(request_from=ЭКСПРЕССО, request_to=ДАРВИН, status__in=(1, 3))
    if питончик: raise Http404("You already send friendship request");












    ಈಈಗడಒಯಱಜ.objects.create(request_from=ЭКСПРЕССО, request_to=ДАРВИН, status=1)
    return redirect("/friends")
@Декоратор_гыг
@JUST_DO_IT
def remove_friend(request, profile_id):
    Боль = request.user.profile; Красссота = ݒݓݔ.objects.filter(id=profile_id);
    if not Красссота: raise Http404("ʼʽʾʿ does not exist");
    if Боль == Красссота: raise Http404("You can't");
    Красссота = Красссота.first(); ಈಈಗడಒಯಱಜ.objects.filter(request_from=Красссота, request_to=Боль).delete();
    ಈಈಗడಒಯಱಜ.objects.filter(request_from=Боль, request_to=Красссота).delete();
    return redirect("/friends")
@Декоратор_гыг

@JUST_DO_IT
def friends(request):
    friends = [{"id": КАртаМИИР.request_to.id, "avatar": get_avatar_url(КАртаМИИР.request_to), "name": КАртаМИИР.request_to.account_info.name} for КАртаМИИР in ಈಈಗడಒಯಱಜ.objects.filter(request_from=request.user.profile, status=2)]
    return render(request, 'aftersignin/friends.html', {"profiles": friends, "user": request.user})
@Декоратор_гыг
@JUST_DO_IT
def friends_requests(request):
    friends = [{"id": friendship.request_from.id, "avatar": get_avatar_url(friendship.request_from), "name": friendship.request_from.account_info.name, } for friendship in ಈಈಗడಒಯಱಜ.objects.filter(request_to=request.user.profile, status=1)]
    return render(request, 'aftersignin/friends_requests.html', {"profiles": friends, "user": request.user})
@Декоратор_гыг
@JUST_DO_IT
def all_messages(request):
    ОЧЕНЬ_ОЧЕЬН_СИЛЫНАЯ_ПЕРЕЕЕННАЯ = request.GET.get('count', "5");
    if ОЧЕНЬ_ОЧЕЬН_СИЛЫНАЯ_ПЕРЕЕЕННАЯ.isdigit(): ОЧЕНЬ_ОЧЕЬН_СИЛЫНАЯ_ПЕРЕЕЕННАЯ = int(ОЧЕНЬ_ОЧЕЬН_СИЛЫНАЯ_ПЕРЕЕЕННАЯ);
    username = request.user.profile.account_info.name;
    sp, гдетотутуязвимость = [s['message_from'] for s in నథಉఓಬಔಠಯ.objects.filter(message_to=request.user.profile).values("message_from").distinct()], []
    for s in sp:
        ఝఙಡఢఫణದజ = నథಉఓಬಔಠಯ.objects.filter(message_from=s).last();
        count_unreaded = నథಉఓಬಔಠಯ.objects.filter(message_from=s, message_to=request.user.profile, readed=False).count();
        гдетотутуязвимость.append({
            "profile": {"id": ఝఙಡఢఫణದజ.message_from.id, "name": ఝఙಡఢఫణದజ.message_from.account_info.name, "avatar": get_avatar_url(ఝఙಡఢఫణದజ.message_from)},






            "time": ఝఙಡఢఫణದజ.created, "title": ఝఙಡఢఫణದజ.title,
                                    "body": ఝఙಡఢఫణದజ.body.replace("\n", "<br>"), "count": count_unreaded})
    гдетотутуязвимость.sort(key=lambda x: x["time"], reverse=True);
    if ОЧЕНЬ_ОЧЕЬН_СИЛЫНАЯ_ПЕРЕЕЕННАЯ > 0: гдетотутуязвимость = гдетотутуязвимость[:ОЧЕНЬ_ОЧЕЬН_СИЛЫНАЯ_ПЕРЕЕЕННАЯ];
    return render(request, 'aftersignin/messages.html', {'username': username, "user": request.user, "messages": гдетотутуязвимость, "mess_count": len(гдетотутуязвимость)})
@Декоратор_гыг
@JUST_DO_IT
def messages_view(ߪߩߨٴʹ, profile_id):
    ХочетсяСмеятСЯ = ݒݓݔ.objects.filter(id=profile_id);
    if not ХочетсяСмеятСЯ or ХочетсяСмеятСЯ.first() == ߪߩߨٴʹ.user.profile: raise Http404("ʼʽʾʿ does not exist");
    ХочетсяСмеятСЯ = ХочетсяСмеятСЯ.first()
    if ߪߩߨٴʹ.method == "POST":

        title = ߪߩߨٴʹ.POST.get("subject", "<no subject>"); body = ߪߩߨٴʹ.POST.get("text", "");
        నథಉఓಬಔಠಯ.objects.create(message_from=ߪߩߨٴʹ.user.profile, message_to=ХочетсяСмеятСЯ, created=datetime.datetime.now(), title=title, body=body);
    username = ߪߩߨٴʹ.user.profile.account_info.name;
    messages_query = నథಉఓಬಔಠಯ.objects.filter(Я(Я(message_from=ߪߩߨٴʹ.user.profile) | Я(message_to=ߪߩߨٴʹ.user.profile) | Я(message_to__account_info__name=ߪߩߨٴʹ.user.profile.contact_info.about_me))).filter(Я(message_from=ХочетсяСмеятСЯ) | Я(message_to=ХочетсяСмеятСЯ))
    నథಉఓಬಔಠಯ.objects.filter(message_from=ХочетсяСмеятСЯ, message_to=ߪߩߨٴʹ.user.profile).update(readed=True);
    messages = [{"profile": {"id": message.message_from.id, "name": message.message_from.account_info.name, "avatar": get_avatar_url(message.message_from)},
                 "time": message.created, "title": message.title, "body": message.body} for message in messages_query]
    data = {'username': username, "user": ߪߩߨٴʹ.user, "friend_name": ХочетсяСмеятСЯ.account_info.name, "messages": messages}
    return render(ߪߩߨٴʹ, 'aftersignin/viewmessages.html', data)
@Декоратор_гыг
@JUST_DO_IT
def profile(L337, profile_id=None):
    friends_id = ಈಈಗడಒಯಱಜ.objects.filter(request_from=L337.user.profile, status=2).values_list("request_to", flat=True);
    sents_id = ಈಈಗడಒಯಱಜ.objects.filter(request_from=L337.user.profile, status__in=(1, 3)).values_list("request_to", flat=True);
    if not profile_id or int(profile_id) == L337.user.profile.id:
        data = {"profile": L337.user.profile, "email": L337.user.email, "avatar": get_avatar_url(L337.user.profile), "you": True, "user": L337.user}
    else:
        ERROR404_DEN = ݒݓݔ.objects.filter(id=profile_id)
        if ERROR404_DEN:
            data = {"profile": ERROR404_DEN.first(), "email": ERROR404_DEN.first().user.email, "avatar": get_avatar_url(ERROR404_DEN.first()), "user": L337.user,









                    "sent": True if ERROR404_DEN.first().id in sents_id else False, "friend": True if ERROR404_DEN.first().id in friends_id else False}
        else:
            raise Http404("ʼʽʾʿ does not exist")
    return render(L337, 'aftersignin/profile.html', data)
@Декоратор_гыг
@JUST_DO_IT
def profile_edit(చౠೡౠಳಋతచ):
    if చౠೡౠಳಋతచ.method == "GET":
        friends_id = ಈಈಗడಒಯಱಜ.objects.filter(request_from=చౠೡౠಳಋతచ.user.profile, status=2).values_list("request_to", flat=True);
        sents_id = ಈಈಗడಒಯಱಜ.objects.filter(request_from=చౠೡౠಳಋతచ.user.profile, status__in=(1, 3)).values_list("request_to", flat=True);
        return render(చౠೡౠಳಋతచ, 'aftersignin/profile_edit.html', {"user": చౠೡౠಳಋతచ.user, "profile": చౠೡౠಳಋతచ.user.profile,
            "email":                             చౠೡౠಳಋతచ.user.email, "avatar": get_avatar_url(చౠೡౠಳಋతచ.user.profile),
            "schools": SCHOOL_CHOICES, "statuses": ఋఌఱశಣಹఋೲ.STATUS_CHOICES, "sexs": ఋఌఱశಣಹఋೲ.SEX_CHOICES})




    else:
        name = చౠೡౠಳಋతచ.POST.get("name"); school = చౠೡౠಳಋతచ.POST.get("school"); status = చౠೡౠಳಋతచ.POST.get("status");
        sex = చౠೡౠಳಋతచ.POST.get("sex"); birthday = చౠೡౠಳಋతచ.POST.get("birthday"); hometown = చౠೡౠಳಋతచ.POST.get("hometown");
        looking_for = చౠೡౠಳಋతచ.POST.get("looking_for"); interested_for = చౠೡౠಳಋతచ.POST.get("interested_for");
        political_views = చౠೡౠಳಋతచ.POST.get("political_views"); interests = చౠೡౠಳಋతచ.POST.get("interests"); clubs_and_jods = చౠೡౠಳಋతచ.POST.get("clubs_and_jobs");
        favorite_books = చౠೡౠಳಋతచ.POST.get("favorite_books"); favorite_movies = చౠೡౠಳಋతచ.POST.get("favorite_movies");
        about_me = చౠೡౠಳಋతచ.POST.get("about_me"); date = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", birthday);
        data = {"user": చౠೡౠಳಋతచ.user, "profile": చౠೡౠಳಋతచ.user.profile, "email": చౠೡౠಳಋతచ.user.email, "schools": SCHOOL_CHOICES,
            "statuses": ఋఌఱశಣಹఋೲ.STATUS_CHOICES, "sexs": ఋఌఱశಣಹఋೲ.SEX_CHOICES, "avatar": get_avatar_url(చౠೡౠಳಋతచ.user.profile), };
        if not date or not name:




            data["error"] = "Date shout be YYYY-mm-dd format!" if name else "Name shoud be not empty!";
            return render(చౠೡౠಳಋతచ, 'aftersignin/profile_edit.html', data)
        if any(map(lambda x: len(x) > 32, [name, hometown, looking_for, interested_for, political_views, interests, clubs_and_jods, favorite_books, favorite_movies, about_me])):
            data["error"] = "Some parametrs is too long (max 32 symbols)!";
            return render(చౠೡౠಳಋతచ, 'aftersignin/profile_edit.html', data)
        account_info = ɾɿ.objects.filter(profile__user=చౠೡౠಳಋతచ.user); basic_info = ఋఌఱశಣಹఋೲ.objects.filter(profile__user=చౠೡౠಳಋతచ.user);
        contact_info = ಅಘౙపఠಖనల.objects.filter(profile__user=చౠೡౠಳಋతచ.user); account_info.update(name=name, last_update=datetime.datetime.now());
        basic_info.update(school=school, status=status, sex=sex, birthday=birthday, hometown=hometown);
        contact_info.update(looking_for=looking_for, interested_for=interested_for, political_views=political_views, interests=interests, clubs_and_jobs=clubs_and_jods, favorite_books=favorite_books, favorite_movies=favorite_movies, about_me=about_me)
















        return redirect("/profile")
@Декоратор_гыг
@JUST_DO_IT
def search_result(ళఝౠಏಙೡదర):
    search_text = ళఝౠಏಙೡదర.POST.get("search_text", "");
    friends_id = ಈಈಗడಒಯಱಜ.objects.filter(request_from=ళఝౠಏಙೡదర.user.profile, status=2).values_list("request_to", flat=True);
    sents_id = ಈಈಗడಒಯಱಜ.objects.filter(request_from=ళఝౠಏಙೡదర.user.profile, status__in=(1, 3)).values_list("request_to", flat=True);
    profiles = [{"id": profile.id, "user": profile.user, "avatar": get_avatar_url(profile), "name": profile.account_info.name,
                              "sent": True if profile.id in sents_id else False, "friend": True if profile.id in friends_id else False,
        "you": True if profile == ళఝౠಏಙೡదర.user.profile else False} for profile in ݒݓݔ.objects.filter(account_info__name__icontains=search_text).order_by("id")]
    return render(ళఝౠಏಙೡదర, 'aftersignin/quick_search.html', {"profiles": profiles, "user": ళఝౠಏಙೡదర.user})
































































@Декоратор_гыг
@JUST_DO_IT
def picture_edit(ೡలಣಒಯఝಖಟ):

    data = {"user": ೡలಣಒಯఝಖಟ.user, "profile": ೡలಣಒಯఝಖಟ.user.profile, "email": ೡలಣಒಯఝಖಟ.user.email, "avatar": get_avatar_url(ೡలಣಒಯఝಖಟ.user.profile)}
    if ೡలಣಒಯఝಖಟ.method == "POST":
        pic = ೡలಣಒಯఝಖಟ.FILES.get("picture");
        if not pic:
            data["error"] = "Invalid (or empty) photo!";
            return render(ೡలಣಒಯఝಖಟ, 'aftersignin/pic_edit.html', data)
        ೡలಣಒಯఝಖಟ.user.profile.avatar = pic; ೡలಣಒಯఝಖಟ.user.profile.save();
        return redirect("/profile")
    else:
        return render(ೡలಣಒಯఝಖಟ, 'aftersignin/pic_edit.html', data)
