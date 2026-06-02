<?php
define('API_KEY',"8890056909:AAGijoauBwE5dL7jEkxegbKbjFnOVdvrPt4");

$builder24 = "2102514325";
$admin = "2102514325";
$admins=file_get_contents("stat/admins.txt");
$admin = explode("\n", $admins);
array_push($admin,$builder24);

function bot($method,$datas=[]){
$url = "https://api.telegram.org/bot".API_KEY."/".$method;
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
$res = curl_exec($ch);
if(curl_error($ch)){
var_dump(curl_error($ch));
}else{
return json_decode($res);
}}

function deleteFolder($path){
if(is_dir($path) === true){
$files = array_diff(scandir($path), array('.', '..'));
foreach ($files as $file)
deleteFolder(realpath($path) . '/' . $file);
return rmdir($path);
}else if (is_file($path) === true)
return unlink($path);
return false;
}

function joinchat($id){
global $mid;
$array = array("inline_keyboard");
$kanallar=file_get_contents("kanal/ch.txt");
if($kanallar == null){
return true;
}else{
$ex = explode("\n",$kanallar);
for($i=0;$i<=count($ex) -1;$i++){
$first_line = $ex[$i];
$first_ex = explode("@",$first_line);
$url = $first_ex[1];
$ism=bot('getChat',['chat_id'=>"@".$url,])->result->title;
$ret = bot("getChatMember",[
"chat_id"=>"@$url",
"user_id"=>$id,
]);
$stat = $ret->result->status;
if((($stat=="creator" or $stat=="administrator" or $stat=="member"))){
$array['inline_keyboard']["$i"][0]['text'] = "✅ ". $ism;
$array['inline_keyboard']["$i"][0]['url'] = "https://t.me/$url";
}else{
$array['inline_keyboard']["$i"][0]['text'] = "❌ ". $ism;
$array['inline_keyboard']["$i"][0]['url'] = "https://t.me/$url";
$uns = true;
}
}
$array['inline_keyboard']["$i"][0]['text'] = "🔄 Tekshirish";
$array['inline_keyboard']["$i"][0]['callback_data'] = "check";
if($uns == true){
bot('sendMessage',[
'chat_id'=>$id,
'text'=>"<b>⚠️ Botdan to'liq foydalanish uchun quyidagi kanallarimizga obuna bo'ling!</b>",
'parse_mode'=>'html',
'disable_web_page_preview'=>true,
'reply_markup'=>json_encode($array),
]);
return false;
}else{
return true;
}}}

$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$cid = $message->chat->id;
$tx = $message->text;
$mid = $message->message_id;
$name1 = $message->from->first_name;
$fid = $message->from->id;
$name = $message->from->first_name;
$callback = $update->callback_query;
$data = $callback->data;
$callid = $callback->id;
$ccid = $callback->message->chat->id;
$cmid = $callback->message->message_id;
$from_id = $update->message->from->id;
$token = $message->text;
$text = $message->text;
$message_id = $callback->message->message_id;
$data = $update->callback_query->data;
$callcid=$update->callback_query->message->chat->id;
$botdel = $update->my_chat_member->new_chat_member; 
$botdelid = $update->my_chat_member->from->id;
$status= $botdel->status;
$doc = $update->message->document;
$doc_id = $doc->file_id;
$cqid = $update->callback_query->id;
$callfrid = $update->callback_query->from->id;
$botname = bot('getme',['bot'])->result->username;
$callname = $update->callback_query->from->first_name;
$frid= $update->callback_query->from->id;
#-----------------------------
if(!file_exists("kabinet/$fid.som")){
file_put_contents("kabinet/$fid.som","0");
}
$som = file_get_contents("kabinet/$fid.som");
if(!file_exists("kabinet/$fid.dpz")){
file_put_contents("kabinet/$fid.dpz","0");
}
$dpz = file_get_contents("kabinet/$fid.dpz");
if(file_get_contents("stat/odam.txt")){
}else{
file_put_contents("stat/odam.txt","");
}
if(file_get_contents("stat/kirit.txt")){
}else{
file_put_contents("stat/kirit.txt","0");
}
$krt = file_get_contents("stat/kirit.txt");
if(file_get_contents("stat/yech.txt")){
}else{
file_put_contents("stat/yech.txt","0");
}
$ych = file_get_contents("stat/yech.txt");
if(file_get_contents("invest/id.txt")){
}else{
file_put_contents("invest/id.txt","0");
}
$sid=file_get_contents("invest/id.txt");
file_put_contents("stat/admins.txt");
if(file_get_contents("stat/payments.txt")){
}else{
file_put_contents("stat/payments.txt","");
}
$pay = file_get_contents("stat/payments.txt");


if(file_get_contents("edit/adminuser.txt")){
}else{
file_put_contents("edit/adminuser.txt","<code>@MrUzbekDev</code>");
}
if(file_get_contents("edit/valyuta.txt")){
}else{
file_put_contents("edit/valyuta.txt","so'm");
}
if(file_get_contents("edit/taklifnarx.txt")){
}else{
file_put_contents("edit/taklifnarx.txt","500");
}
if(file_get_contents("edit/minyech.txt")){
}else{
file_put_contents("edit/minyech.txt","5000");
}

if(file_get_contents("tugma/tugma1.txt")){
}else{
file_put_contents("tugma/tugma1.txt","➕ Mining sotib olish");
}
if(file_get_contents("tugma/tugma2.txt")){
}else{
file_put_contents("tugma/tugma2.txt","💰 Hisobim");
}
if(file_get_contents("tugma/tugma3.txt")){
}else{
file_put_contents("tugma/tugma3.txt","💵 Pul ishlash");
}
if(file_get_contents("tugma/tugma4.txt")){
}else{
file_put_contents("tugma/tugma4.txt","📚 Ma'lumot");
}
if(file_get_contents("tugma/tugma5.txt")){
}else{
file_put_contents("tugma/tugma5.txt","📝 Murojaat");
}

$investmt = str_replace(["%inson%","%stat%"], [$calluser,$u],file_get_contents("matn/stat.txt"));

$tugma1 = file_get_contents("tugma/tugma1.txt");
$tugma2 = file_get_contents("tugma/tugma2.txt");
$tugma3 = file_get_contents("tugma/tugma3.txt");
$tugma4 = file_get_contents("tugma/tugma4.txt");
$tugma5 = file_get_contents("tugma/tugma5.txt");

$minyech = file_get_contents("edit/minyech.txt");
$taklifpul = file_get_contents("edit/taklifnarx.txt");
$valyuta = file_get_contents("edit/valyuta.txt");
$admin_user = file_get_contents("edit/adminuser.txt");
#-----------------------------
mkdir("kabinet");
mkdir("invest");
mkdir("tugma");
mkdir("matn");
mkdir("sozlamalar");
mkdir("sozlamalar/number");
mkdir("sozlamalar/hamyon");
mkdir("tarif");
mkdir("step");
mkdir("stat");
mkdir("ban");
mkdir("edit");
#-----------------------------

$ban = file_get_contents("ban/$fid.txt");
$stat=file_get_contents("stat/odam.txt");
$userstep=file_get_contents("step/$fid.txt");
$soat=date("H:i",strtotime("2 hour"));

if($tx){
if($ban == "ban"){
exit();
}else{
}}

if($data){
$ban = file_get_contents("ban/$ccid.txt");
if($ban == "ban"){
exit();
}else{
}}

if(isset($message)){
$get = file_get_contents("stat/odam.txt");
if(mb_stripos($get,$fid)==false){
file_put_contents("stat/odam.txt",  "$get\n$fid");
}}

if($botdel){
if($status=="kicked"){
$get = file_get_contents("stat/odam.txt");
if(mb_stripos($get,$botdelid)==false){
$oladi=str_replace("\n".$botdelid."","",$get);
file_put_contents("stat/odam.txt", $oladi);
unlink("kabinet/$botdelid.txt");
unlink("kabinet/$botdelid.dpz");
unlink("kabinet/$botdelid.som");
}}}

if(mb_stripos($text,"/start")!==false){
$refid = explode(" ",$text);
$refid = $refid[1];
if(strlen($refid)>0 and $refid>0){
if($refid == $cid){
bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>Start matn</b>",
'parse_mode'=>'html',
'reply_markup'=>$menyu,
]);
exit();
}else{
if(mb_stripos($stat,"$cid")!==false){
bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>Start matn</b>",
'parse_mode'=>'html',
'reply_markup'=>$menyu,
]);
exit();
}else{
bot('SendMessage',[
'chat_id'=>$refid,
'text'=>"<b>Taklif matn</b>",
'parse_mode'=>'html',
]);
$odam = file_get_contents("kabinet/$refid.odam");
$odam1 = $odam + 1;
file_put_contents("kabinet/$refid.odam", $odam1);
$puli = file_get_contents("kabinet/$refid.som");
$pullar = $puli + 555;
file_put_contents("kabinet/$refid.som", $pullar);
file_put_contents("kabinet/$cid.txt","$refid");
exit();
}}}}

date_default_timezone_set('Asia/Tashkent'); 
$sana=date("d"); 
$topiladi=glob("invest/*/ish.kun"); 
foreach($topiladi as $topildi){ 
$id=str_replace(["invest/","/ish.kun"],["",""],$topildi); 
$vaqti = json_decode(file_get_contents("invest/$id/ish.kun")); 
echo $vaqti->kun; 
if($vaqti->sana!=$sana){
$invest["sana"]=$sana;
$invest["kun"]=$vaqti->kun-1; 
file_put_contents("invest/$id/ish.kun",json_encode($invest)); 
$qow=file_get_contents("invest/$id/kun.txt");
$cid=file_get_contents("invest/$id/ega.txt");
$pul = file_get_contents("kabinet/$cid.som");
$w = $pul + $qow;
file_put_contents("kabinet/$cid.som",$w);
$plus=file_get_contents("stat/day.txt");
$plus +=1;
file_put_contents("stat/day.txt",$plus);
}
if($vaqti->kun==0 or $vaqti->kun<=0){
$qow=file_get_contents("invest/$id/chiq.txt");
$cid=file_get_contents("invest/$id/ega.txt");
$pul = file_get_contents("kabinet/$cid.som");
$m = $pul + $qow;
file_put_contents("kabinet/$cid.som",$m);
deleteFolder("invest/$id");
}}

$main_menu = json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"$tugma1"]],
[['text'=>"$tugma2"],['text'=>"$tugma3"]],
[['text'=>"$tugma4"],['text'=>"$tugma5"]],
]]);

$main_menuad = json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"$tugma1"]],
[['text'=>"$tugma2"],['text'=>"$tugma3"]],
[['text'=>"$tugma4"],['text'=>"$tugma5"]],
[['text'=>"🗄 Boshqarish"]],
]]);

$panel = json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"⚙ Asosiy sozlamalar"]],
[['text'=>"📢 Kanallar"]NARUTO-MODZ-1A2B,['text'=>"📈 Investitsiya"]],
[['text'=>"🔎 Foydalanuvchini boshqarish"]],
[['text'=>"🎛 Tugmalar"],['text'=>"📑 Matnlar"]],
[['text'=>"🎁 Kunlik bonus sozlamalari"]],
[['text'=>"📩 Xabarnoma"],['text'=>"📊 Statistika"]],
[['text'=>"◀️ Orqaga"]],
]]);

if(in_array($cid,$admin)){
$menyu = $main_menuad;
}
if(in_array($cid,$admin)){
}else{
$menyu = $main_menu;
}

if(in_array($ccid,$admin)){
$menyus = $main_menuad;
}
if(in_array($ccid,$admin)){
}else{
$menyus = $main_menu;
}

if($tx=="*⃣ Birlamchi sozlamalar" and in_array($cid,$admin)){
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>*⃣ Birlamchi sozlamalar bo'limiga xush kelibsiz!</b>

<i>Nimani o'zgartiramiz?</i>",
'parse_mode'=>"html",
'reply_markup'=> json_encode([
'inline_keyboard'=>[
[['text'=>"📋 Hozirgi holat",'callback_data'=>"hozirgi_holat"]],
[['text'=>"💳 Minimal pul yechish narxi",'callback_data'=>"minyech"],['text'=>"🔐 Admin useri",'callback_data'=>"admin_user"]],
[['text'=>"🔗 Taklif narxi",'callback_data'=>"taklif_narxi"],['text'=>"💶 Valyuta nomi",'callback_data'=>"valyuta_nomi"]],
]])
]);
}

if($data=="birlamchi"){
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>*⃣ Birlamchi sozlamalar bo'limiga xush kelibsiz!</b>

<i>Nimani o'zgartiramiz?</i>",
'parse_mode'=>"html",
'reply_markup'=> json_encode([
'inline_keyboard'=>[
[['text'=>"📋 Hozirgi holat",'callback_data'=>"hozirgi_holat"]],
[['text'=>"💳 Minimal pul yechish narxi",'callback_data'=>"minyech"],['text'=>"🔐 Admin useri",'callback_data'=>"admin_user"]],
[['text'=>"🔗 Taklif narxi",'callback_data'=>"taklifnarx"],['text'=>"💶 Valyuta nomi",'callback_data'=>"valyuta"]],
]])
]);
}

if($data=="taklifnarx"){
$holat = file_get_contents("edit/taklifnarx.txt");
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Hozirgi holat:</b> $holat

<i>Yangi qiymatni yuboring:</i>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("edit.txt","taklifnarx");
}

if($edit == "taklifnarx"){
if($tx=="🗄 Boshqarish"){
unlink("edit.txt");
}else{
file_put_contents("edit/taklifnarx.txt","$tx");
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Qabul qilindi!</b>

<i>Tugma nomi</i> <b>$tx</b> <i>ga o'zgartirildi</i>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
unlink("edit.txt");
}}

if($data=="valyuta"){
$holat = file_get_contents("edit/valyuta.txt");
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Hozirgi holat:</b> $holat

<i>Yangi qiymatni yuboring:</i>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("edit.txt","valyuta");
}

if($edit == "valyuta"){
if($tx=="🗄 Boshqarish"){
unlink("edit.txt");
}else{
file_put_contents("edit/valyuta.txt","$tx");
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Qabul qilindi!</b>

<i>Tugma nomi</i> <b>$tx</b> <i>ga o'zgartirildi</i>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
unlink("edit.txt");
}}

if($data=="admin_user"){
$holat = file_get_contents("edit/admin_user.txt");
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Hozirgi holat:</b> $holat

<i>Yangi qiymatni yuboring:</i>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("edit.txt","admin_user");
}

if($edit == "admin_user"){
if($tx=="🗄 Boshqarish"){
unlink("edit.txt");
}else{
file_put_contents("edit/admin_user.txt","$tx");
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Qabul qilindi!</b>

<i>Tugma nomi</i> <b>$tx</b> <i>ga o'zgartirildi</i>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
unlink("edit.txt");
}}


$edit=file_get_contents("edit.txt");
if($data=="minyech"){
$holat = file_get_contents("edit/minyech.txt");
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Hozirgi holat:</b> $holat

<i>Yangi qiymatni yuboring:</i>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("edit.txt","minyech");
}

if($edit == "minyech"){
if($tx=="🗄 Boshqarish"){
unlink("edit.txt");
}else{
file_put_contents("edit/minyech.txt","$tx");
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Qabul qilindi!</b>

<i>Tugma nomi</i> <b>$tx</b> <i>ga o'zgartirildi</i>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
unlink("edit.txt");
}}

if($data=="hozirgi_holat"){
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>Hozirgi holat:</b>

<b>1. Valyuta:</b> $valyuta
<b>2. Taklif narxi:</b> $taklifpul $valyuta
<b>2. Admin useri:</b> $admin_user
<b>3. Pul yechish narxi:</b> $minyech $valyuta",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"birlamchi"]],
]])
]);
}


if($tx == "⚙ Asosiy sozlamalar" and in_array($cid,$admin)){
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>⚙ Asosiy sozlamalar bo'limiga xush kelibsiz!</b>

<i>Nimani o'zgartiramiz?</i>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"*⃣ Birlamchi sozlamalar"]],
[['text'=>"💳 Hamyonlar"],['text'=>"👤 Adminlar"]],
[['text'=>"💵 Yechish tizimi"],['text'=>"🗄 Boshqarish"]],
]])
]);
}

if($tx=="/start" or $tx=="◀️ Orqaga"){
bot('Sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>Start matn</b>",
'parse_mode'=>"html",
'reply_markup'=>$menyu,
]);
unlink("step/$cid.txt");
exit();
}

if($tx=="$tugma1"){
bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>Key1 matn</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"Kunlik daromad",'callback_data'=>"kunlik_dr"],['text'=>"Standard daromad",'callback_data'=>"standard_dr"]],
[['text'=>"🛒 Investitsiyalarim",'callback_data'=>"my_invest"]],
]])
]);
exit();
}

if($data=="key1"){
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('Sendmessage',[
'chat_id'=>$ccid,
'text'=>"<b>Key1 matn</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"Kunlik daromad",'callback_data'=>"kunlik_dr"],['text'=>"Standard daromad",'callback_data'=>"standard_dr"]],
[['text'=>"🛒 Investitsiyalarim",'callback_data'=>"my_invest"]],
]])
]);
exit();
}

if($data=="my_invest"){
bot('deleteMessage',[ 
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>🆔 Tekshiruv IDsini yuboring:</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"◀️ Orqaga"]]
]])
]);
file_put_contents("step/$ccid.txt","intop");
exit();
}
if($userstep=="intop"){
if($text=="◀️ Orqaga"){
unlink("step/$cid.txt");
}else{
$inv=file_get_contents("invest/$tx/ega.txt");
if($inv != null){
if($inv==$cid){
$kir=file_get_contents("invest/$tx/kir.txt");
$ciq=file_get_contents("invest/$tx/chiq.txt");
$kdr=file_get_contents("invest/$tx/kun.txt");
$xolat=json_decode(file_get_contents("invest/$tx/ish.kun"));
$kun = $xolat->kun;
$times = "$sana — $soat";
$b_time = explode(" — ",$times)[1];
$s_time = explode(":",$b_time)[0]*60;
$m_time = explode(":",$b_time)[1];
$minutes = $s_time + $m_time;
$minus = 24*60;
$qoldi = ($minus - $minutes)*60;
$hours = str_pad(floor($qoldi / (60*60)), 2, '0', STR_PAD_LEFT);
$minutes = str_pad(floor(($qoldi - $hours*60*60)/60), 2, '0', STR_PAD_LEFT);
if($ciq){
$matn="<b>✅ Investitsiya topildi!</b>

<b>▫️ Kiritilgan summa:</b> $kir so'm
<b>▫️ Umumiy daromad:</b> $ciq so'm

Tugash vaqti: {$kun}kun {$hours}soat {$minutes}daqiqa";
}else{
$matn="<b>✅ Investitsiya topildi!</b>

<b>▫️ Kiritilgan summa:</b> $kir so'm
<b>▫️ Kunlik daromad:</b> $kdr so'm

Tugash vaqti: {$kun}kun {$hours}soat {$minutes}daqiqa";
}
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>$matn,
'parse_mode'=>"html",
'reply_markup'=>$menyu,
]);
unlink("step/$cid.txt");
exit();
}else{
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>⚠️ Ushbu investitsiya sizga tegishli emas!</b>",
'parse_mode'=>"html",
]);
exit();
}}else{
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>⚠️ Investitsiya topilmadi!</b>",
'parse_mode'=>"html",
]);
exit();
}}}

if($data=="kunlik_dr"){
$tarif=file_get_contents("tarif/kunlik.txt");
if($tarif == null){
bot('answerCallbackQuery',[
'callback_query_id'=>$callid,
'text'=>"🤷🏻‍♂ Hech qanday tariflar topilmadi!",
'show_alert'=>true,
]);
}else{
$s=explode("\n",$tarif);
$soni = substr_count($tarif,"\n");
$key=[];
for($i=1;$i<=$soni;$i++){
$tikpul=file_get_contents("tarif/".$s[$i]."/krt.pul");
$kunpul=file_get_contents("tarif/".$s[$i]."/kun.pul");
$kun=file_get_contents("tarif/".$s[$i]."/ish.kun");
$umumiy=$kunpul*$kun;
$key[]=["text"=>"$tikpul so'm -> $umumiy so'm ($kun kun)","callback_data"=>"kundr=".$s[$i]];
}
$keysboard2 = array_chunk($key, 1);
$keysboard2[] = [['text'=>"◀️ Orqaga",'callback_data'=>"key1"]];
$tariflar = json_encode([
'inline_keyboard'=>$keysboard2,
]);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>⬇️ Quyidagi tarflardan birini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>$tariflar
]);
exit();
}}

if(mb_stripos($data, "kundr=")!==false){
$ex = explode("=",$data);
$tarif = $ex[1];
$krt = file_get_contents("tarif/$tarif/krt.pul");
$day = file_get_contents("tarif/$tarif/kun.pul");
$kun = file_get_contents("tarif/$tarif/ish.kun");
$umumiy=$day*$kun;
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"💰 <b>Tarif nomi: <u>$tarif</u></b>

▫️ <b>Sarmoya narxi:</b> $krt so'm
▫️ <b>Jami daromad:</b> $umumiy so'm
▫️ <b>Kunlik daromad:</b> $day so'm

Sarmoya kiritsangiz $kun kun davomida kunlik $day so'm hisobingizga qo'shilib boradi!",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"Sarmoya kiritish",'callback_data'=>"invest1=$krt=$day=$kun"]],
[['text'=>"◀️ Orqaga",'callback_data'=>"kunlik_dr"]],
]])
]);
}

if($data=="standard_dr"){
$tarif = file_get_contents("tarif/standard.txt");
if($tarif == null){
bot('answerCallbackQuery',[
'callback_query_id'=>$callid,
'text'=>"🤷🏻‍♂ Hech qanday tariflar topilmadi!",
'show_alert'=>true,
]);
}else{
$s=explode("\n",$tarif);
$soni = substr_count($tarif,"\n");
$key=[];
for($i=1;$i<=$soni;$i++){
$krt=file_get_contents("tarif/".$s[$i]."/krt.pul");
$oln=file_get_contents("tarif/".$s[$i]."/oln.pul");
$kun=file_get_contents("tarif/".$s[$i]."/ish.kun");
$key[]=["text"=>"$krt so'm -> $oln so'm ($kun kun)","callback_data"=>"standr=".$s[$i]];
}
$keysboard2 = array_chunk($key, 1);
$keysboard2[] = [['text'=>"◀️ Orqaga",'callback_data'=>"key1"]];
$tariflar = json_encode([
'inline_keyboard'=>$keysboard2,
]);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>⬇️ Quyidagi tarflardan birini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>$tariflar
]);
exit();
}}

if(mb_stripos($data, "standr=")!==false){
$ex = explode("=",$data);
$tarif = $ex[1];
$krt = file_get_contents("tarif/$tarif/krt.pul");
$oln = file_get_contents("tarif/$tarif/oln.pul");
$kun = file_get_contents("tarif/$tarif/ish.kun");
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"💰 <b>Tarif nomi: <u>$tarif</u></b>

▫️ <b>Sarmoya narxi:</b> $krt so'm
▫️ <b>Jami daromad:</b> $oln so'm

Daromad $kun kun kutiladi va tugaganidan so'ng hisobingizga avtomatik qo'shiladi!",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"Sarmoya kiritish",'callback_data'=>"invest2=$krt=$oln=$kun"]],
[['text'=>"◀️ Orqaga",'callback_data'=>"standard_dr"]],
]])
]);
}

if(mb_stripos($data, "invest1=")!==false){
$ex = explode("=",$data);
$miqdor = $ex[1];
$kunlik = $ex[2];
$kun = $ex[3];
$pulim=file_get_contents("kabinet/$ccid.som");
if($miqdor>$pulim){
bot("answerCallbackQuery",[
'callback_query_id'=>$callid,
'text'=>"⚠️ Mablag' yetarli emas!",
'show_alert'=>true,
]);
}else{
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
$pulim-= $miqdor;
file_put_contents("kabinet/$ccid.som",$pulim);
$ids=file_get_contents("invest/id.txt");
$ids+=1;
file_put_contents("invest/id.txt",$ids);
mkdir("invest/$ids");
file_put_contents("invest/$ids/kun.txt","$kunlik");
file_put_contents("invest/$ids/kir.txt","$miqdor");
file_put_contents("invest/$ids/ega.txt","$ccid");
date_default_timezone_set('Asia/Tashkent');
$day=date("d");
$invest['sana']=$day;
$invest['kun']=$kun;
file_put_contents("invest/$ids/ish.kun",json_encode($invest));
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>✅ Investitsiya qabul qilindi!

🆔 Tekshiruv IDsi:</b> <code>$ids</code>",
'parse_mode'=>"html",
'reply_markup'=>$menyus,
]);
exit();
}}

if(mb_stripos($data, "invest2=")!==false){
$ex = explode("=",$data);
$miqdor = $ex[1];
$umumiy = $ex[2];
$kun = $ex[3];
$pulim=file_get_contents("kabinet/$ccid.som");
if($miqdor>$pulim){
bot("answerCallbackQuery",[
'callback_query_id'=>$callid,
'text'=>"⚠️ Mablag' yetarli emas!",
'show_alert'=>true,
]);
}else{
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
$pulim-= $miqdor;
file_put_contents("kabinet/$ccid.som",$pulim);
$ids=file_get_contents("invest/id.txt");
$ids+=1;
file_put_contents("invest/id.txt",$ids);
mkdir("invest/$ids");
file_put_contents("invest/$ids/chiq.txt","$umumiy");
file_put_contents("invest/$ids/kir.txt","$miqdor");
file_put_contents("invest/$ids/ega.txt","$ccid");
date_default_timezone_set('Asia/Tashkent');
$day=date("d");
$invest['sana']=$day;
$invest['kun']=$kun;
file_put_contents("invest/$ids/ish.kun",json_encode($invest));
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>✅ Investitsiya qabul qilindi!

🆔 Tekshiruv IDsi:</b> <code>$ids</code>",
'parse_mode'=>"html",
'reply_markup'=>$menyus,
]);
exit();
}}

if($tx=="$tugma2" and joinchat($cid)=="true"){
if(in_array($cid,$admin)){
$odam="Adminstrator";
}else{
$odam="Foydalanuvchi";
}
$taklif=file_get_contents("kabinet/$cid.txt");
if($taklif){
$name="<a href='tg://user?id=$taklif'>$taklif </a>";
}else{
$name="Hech kim";
}
bot('Sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>🏛 Sizning botdagi kabinetingiz
├
├Botdagi vazifa:</b> $odam
<b>├ID raqamingiz:</b> <code>$cid</code>
<b>├Asosiy balans:</b> $som so'm
<b>├Depozitingiz:</b> $dpz so'm
<b>├Sizni taklif qildi:</b> $name
├
<b>└@$botname - Yuqori daromad!</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"📤 Pul kiritish",'callback_data'=>"kiritish"],['text'=>"📥 Pul yechish",'callback_data'=>"yechish"]],
[['text'=>"💰 Pul ishlash",'callback_data'=>"ishlash"],['text'=>"🔄 O'tkazma",'callback_data'=>"otqazma"]],
]])
]);
exit();
}

//kartalar
$yechturi=file_get_contents("sozlamalar/number/turi.txt");
$delmore = explode("\n",$yechturi);
$delsoni = substr_count($yechturi,"\n");
$key=[];
for ($delfor = 1; $delfor <= $delsoni; $delfor++) {
$title=str_replace("\n","",$delmore[$delfor]);
$key[]=["text"=>"$title - ni o'chirish","callback_data"=>"del-$title"];
$keyboard2 = array_chunk($key, 1);
$keyboard2[] = [['text'=>"➕ Yechish tizimi qo'shish",'callback_data'=>"new"]];
$pay2 = json_encode([
'inline_keyboard'=>$keyboard2,
]);
}

if($text == "💵 Yechish tizimi" and in_array($cid,$admin)){
if($yechturi == null){
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Quyidagilardan birini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"➕ Yechish tizimi qo'shish",'callback_data'=>"new"]],
]])
]);
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Quyidagilardan birini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>$pay2,
]);
}}

if($data == "tolovtizim"){
if($yechturi == null){
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('SendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Quyidagilardan birini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"➕ Yechish tizimi qo'shish",'callback_data'=>"new"]],
]])
]);
}else{
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('SendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Quyidagilardan birini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>$pay
]);
}}

if(mb_stripos($data,"del-")!==false){
$ex = explode("-",$data);
$tur = $ex[1];
$royxat = file_get_contents("sozlamalar/number/turi.txt");
$k = str_replace("\n".$tur."","",$royxat);
file_put_contents("sozlamalar/number/turi.txt",$k);
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"$tur - <b>Yechish tizimi o'chirildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"tolovtizim"]],
]])
]);
}

if($data == "new"){
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Yechish to'lov tizimi nomini yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$ccid.txt",'turi');
}

if($userstep == "turi"){
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
if(isset($text)){
$yechturi=file_get_contents("sozlamalar/number/turi.txt");
file_put_contents("sozlamalar/number/turi.txt","$yechturi\n$text");
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>To'lov tizimi qo'shildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$admin1_menu,
]);
unlink("step/$cid.txt");
}}}

if($tx=="💳 Hamyonlar" and in_array($cid,$admin)){
$kategoriya = file_get_contents("sozlamalar/hamyon/kategoriya.txt");
$more = explode("\n",$kategoriya);
$soni = substr_count($kategoriya,"\n");
$keys=[];
for ($for = 1; $for <= $soni; $for++) {
$title=str_replace("\n","",$more[$for]);
$keys[]=["text"=>"$title- ni o'chirish","callback_data"=>"delete-$title"];
$keysboard2 = array_chunk($keys, 1);
$keysboard2[] = [['text'=>"➕ Yangi to'lov tizimi qo'shish",'callback_data'=>"yangi_tolov"]];
$key = json_encode([
'inline_keyboard'=>$keysboard2,
]);
}
if($kategoriya != null){
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Quyidagilardan birini tanlang:</b>",
'parse_mode'=>"html",
'reply_markup'=>$key,
]);
}else{
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Quyidagilardan birini tanlang:</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"➕ Yangi to'lov tizimi qo'shish",'callback_data'=>"yangi_tolov"]],

]])
]);
}}

if(mb_stripos($data, "delete-")!==false){
$ex = explode("-",$data);
$kat = $ex[1];
$royxat = file_get_contents("sozlamalar/hamyon/kategoriya.txt");
$k = str_replace("\n".$kat."","",$royxat);
file_put_contents("sozlamalar/hamyon/kategoriya.txt",$k);
deleteFolder("sozlamalar/hamyon/$kat");
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('SendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>To'lov tizimi o'chirildi!</b>",
'parse_mode'=>'html',
]);
}

if($data== "yangi_tolov"){
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('SendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Yangi to'lov tizimi nomini yuboring:

Masalan:</b> Click",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$ccid.txt","tolov");
}

if($userstep=="tolov"){
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
if(isset($text)){
$kategoriya2 = file_get_contents("sozlamalar/hamyon/kategoriya.txt");
file_put_contents("sozlamalar/hamyon/kategoriya.txt","$kategoriya2\n$text");
mkdir("sozlamalar/hamyon/$text");
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Ushbu to'lov tizimidagi hamyoningiz raqamini yuboring:</b>",
'parse_mode'=>'html',
]);
file_put_contents("step/$cid.txt","raqam-$text");
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Yangi to'lov tizimi nomini yuboring:

Masalan:</b> Click",
'parse_mode'=>'html',
]);
}}}

if(mb_stripos($userstep, "raqam-")!==false){
$ex = explode("-",$userstep);
$kat = $ex[1];
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
unlink("sozlamalar/hamyon/$kat");
}else{
file_put_contents("sozlamalar/hamyon/$kat/raqam.txt",$text);
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Yangi to'lov tizimi qo'shildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$admin1_menu,
]);
unlink("step/$cid.txt");
}}


$turi = file_get_contents("sozlamalar/number/turi.txt");
$more = explode("\n",$turi);
$soni = substr_count($turi,"\n");
$keys=[];
for ($for = 1; $for <= $soni; $for++) {
$title=str_replace("\n","",$more[$for]);
$keys[]=["text"=>"$title","callback_data"=>"pay-$title"];
$keysboard2 = array_chunk($keys, 2);
$keysboard2[] = [['text'=>"◀️ Orqaga",'callback_data'=>"orqaga12"]];
$pay = json_encode([
'inline_keyboard'=>$keysboard2,
]);
}

if($data == "yechish"){
$turi = file_get_contents("sozlamalar/number/turi.txt");
if($turi != null){
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('SendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>💳 Pul yechish tizimlaridan birini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>$pay
]);
}else{
bot('answerCallbackQuery',[
'callback_query_id'=>$callid,
'text'=>"⚠️ Pul yechish tizimlari qo'shilmagan!",
'show_alert'=>true,
]);
}}

if(mb_stripos($data, "pay-")!==false){
$ex = explode("-",$data);
$wallet = $ex[1];
$pulim = file_get_contents("kabinet/$ccid.som");
if($pulim>=$minpul){
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('SendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>✅ $wallet qabul qilindi!</b>

Hamyon raqamini yuboring:",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"◀️ Orqaga"]],
]])
]);
file_put_contents("step/$ccid.txt","wallet-$wallet");
}else{
bot('answerCallbackQuery',[
'callback_query_id'=>$callid,
'text'=>"⚠️ Minimal pul yechish narxi: $minpul $pul",
'show_alert'=>true,
]);
}}

if(mb_stripos($userstep, "wallet-")!==false){
$ex = explode("-",$userstep);
$wallet = $ex[1];
if($tx=="◀️ Orqaga"){
unlink("step/$cid.txt");
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>❕Qancha pul yechmoqchisiz?</b>

<b>Asosiy balans:</b> $som $pul (komissa 5%)",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"◀️ Orqaga"]],
]])
]);
file_put_contents("step/$cid.txt","miqdor-$wallet-$text");
}}

if(mb_stripos($userstep, "miqdor-")!==false){
$ex = explode("-",$userstep);
$wallet = $ex[1];
$num = $ex[2];
$foiz = $text/100*5;
$miqdor = $text - $foiz;
if($tx=="◀️ Orqaga"){
unlink("step/$cid.txt");
}else{
if($text >= $minpul){
if($som >= $text){
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"✅ <b>Qabul qilindi!</b>\n\n• <b>To'lov turi:</b> $wallet\n• <b>Pul miqdori:</b> $miqdor $pul\n• <b>Hamyon raqamingiz:</b> $num\n\n<b>Ma'lumotlar to'g'ri ekanligiga ishonch hosil qilgan bo'lsangiz, ✅ Tasdiqlash tugmasini bosing!</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"✅ Tasdiqlash",'callback_data'=>"tasdiq-$wallet-$num-$miqdor"]],
[['text'=>"❌ Bekor qilish",'callback_data'=>"bekor"]]
]])
]);
unlink("step/$cid.txt");
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"⚠️ <b>Hisobingizda mablag'yetarli emas!</b>",
'parse_mode'=>'html',
]);
}}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>⚠️ Minimal pul yechish narxi: $minpul $pul</b>",
'parse_mode'=>'html',
]);
}}}

if($data == "bekor"){
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('SendMessage',[
'chat_id'=>$ccid,
'text'=>"$start",
'parse_mode'=>'html',
'reply_markup'=>$menyus,
]);
}

if(mb_stripos($data, "tasdiq-")!==false){
$ex = explode("-",$data);
$wallet = $ex[1];
$number = $ex[2];
$miqdor = $ex[3];
$pul = file_get_contents("kabinet/$ccid.som");
$m = $pul - $miqdor;
file_put_contents("kabinet/$ccid.som",$m);
$zayafka = file_get_contents("foydalanuvchilar/$ccid.zayafka");
if(stripos("$zayafka","$callfrid") !== false){
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"start",
'parse_mode'=>"html",
'reply_markup'=>$menyus,
]);
unlink("step/$ccid.txt");
}else{
file_put_contents("foydalanuvchilar/$ccid.zayafka","\n".$callfrid,FILE_APPEND);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>✉️ Pul yechib olish uchun adminga ariza yuborildi!</b>",
'parse_mode'=>"html",
'reply_markup'=>$menyus,
]);
unlink("step/$ccid.txt");
bot('SendMessage',[
'chat_id'=>$builder24,
'text'=>"💵 <a href='tg://user?id=$ccid'>$ccid</a> <b>pul yechib olmoqchi!</b>

• <b>To'lov turi:</b> $wallet
• <b>Pul miqdori:</b> $miqdor
• <b>Hamyon raqami:</b> $number",
'disable_web_page_preview'=>true,
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"✅ To'landi",'callback_data'=>"tolandi-$ccid-$number-$miqdor"],['text'=>"❌ To'lanmadi",'callback_data'=>"tolanmadi-$ccid-$miqdor"]],
]])
]);
}}

if(mb_stripos($data,"tolandi-")!==false){
$ex = explode("-",$data);
$id = $ex[1];
$number = $ex[2];
$miqdor = $ex[3];
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('SendMessage',[
'chat_id'=>$builder24,
'text'=>"<a href='tg://user?id=$id'>Foydalanuvchi</a><b> $miqdor $pul puli to'lab berildi!</b>",
'parse_mode'=>'html',
]);
bot('sendMessage',[
'chat_id'=>$yangi,
'text'=>"<b>🔹 Foydalanuvchi: <u>$id</u> puli $miqdor $pul to'lab berildi!</b>",
'parse_mode'=>'html',
"reply_markup"=>json_encode([
'inline_keyboard'=>[
[['text'=>"🔹 Foydalanuvchi",'url'=>"tg://user?id=$id"]],
]])
]);
bot('SendMessage',[
'chat_id'=>$id,
'text'=>"<b>✅ Pullaringiz to'lab berildi</b>

<i>Biz bilan bo'ling va pullaringizni hech qanday sarflashlarsiz ko'paytiring!</i>",
'parse_mode'=>'html',
]);
unlink("foydalanuvchi/zayafka.$id");
}

if(mb_stripos($data,"tolanmadi-")!==false){
$ex = explode("-",$data);
$id = $ex[1];
$miqdor = $ex[2];
$pul = file_get_contents("kabinet/$id.som");
$m = $pul + $miqdor;
file_put_contents("kabinet/$id.som",$m);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('SendMessage',[
'chat_id'=>$builder24,
'text'=>"<a href='tg://user?id=$id'>Foydalanuvchi</a> <b>arizasi bekor qilindi!</b>",
'parse_mode'=>'html',
]);
bot('SendMessage',[
'chat_id'=>$id,
'text'=>"<b>⚠️ Arizangiz bekor qilindi!</b>",
'parse_mode'=>'html',
]);
unlink("foydalanuvchi/zayafka.$id");
}


if($data=="kiritish"){
$kategoriya = file_get_contents("sozlamalar/hamyon/kategoriya.txt");
$more = explode("\n",$kategoriya);
$soni = substr_count($kategoriya,"\n");
$key=[];
for ($for = 1; $for <= $soni; $for++) {
$title = str_replace("\n","",$more[$for]);
$key[]=["text"=>"$title","callback_data"=>"karta-$title"];
$keyboard2 = array_chunk($key, 2);
$keyboard2[] = [['text'=>"◀️ Orqaga",'callback_data'=>"orqaga12"]];
$bolim = json_encode([
'inline_keyboard'=>$keyboard2,
]);
}
if($kategoriya == null){
bot("answerCallbackQuery",[
"callback_query_id"=>$callid,
"text"=>"⚠️ To'lov tizimlari qo'shilmagan!",
"show_alert"=>true,
]);
}else{
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>💳 To'lov tizimlaridan birini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>$bolim,
]);
}}

if(mb_stripos($data, "karta-")!==false){
$ex = explode("-",$data);
$kategoriya = $ex[1];
$raqam = file_get_contents("sozlamalar/hamyon/$kategoriya/raqam.txt");
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>📲 To‘lov turi:</b> <u>$kategoriya</u>

💳 Karta: <code>$raqam</code>
📝 Izoh: #ID$ccid

Almashuvingiz muvaffaqiyatli bajarilishi uchun quyidagi harakatlarni amalga oshiring: 
1) Istalgan pul miqdorini tepadagi Hamyonga tashlang
2) «✅ To'lov qildim» tugmasini bosing; 
4) Qancha pul miqdoni yuborganingizni kiritin;
3) Toʻlov haqidagi suratni botga yuboring;
3) Operator tomonidan almashuv tasdiqlanishini kuting!",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"✅ To'lov qildim",'callback_data'=>"tolov"]],
[['text'=>"◀️ Orqaga",'callback_data'=>"oplata"]],
]])
]);
}

if($data == "tolov"){
bot('DeleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('SendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>📝 To'lov miqdorini yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"◀️ Orqaga"]],
]])
]);
file_put_contents("step/$ccid.txt",'oplata');
}

if($userstep == "oplata"){
if($tx=="◀️ Orqaga"){
unlink("step/$cid.txt");
}else{
file_put_contents("step/hisob.$cid",$text);
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>🧾 To'lovingiz haqidagi chekni shu yerga yuboring:</b>",
'parse_mode'=>'html',
]);
file_put_contents("step/$cid.txt",'rasm');
}}

if($userstep == "rasm"){
if($tx=="◀️ Orqaga"){
unlink("step/$fid.txt");
}else{
$photo = $message->photo;
$file = $photo[count($photo)-1]->file_id;
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>💌 So'rovingiz adminga yuborildi!</b>

<i>Biroz kuting...</i>",
'parse_mode'=>'html',
'reply_markup'=>$menyu,
]);
$hisob=file_get_contents("step/hisob.$fid");
unlink("step/$fid.txt");
bot('sendPhoto',[
'chat_id'=>$builder24,
'photo'=>$file,
'caption'=>"📄 <b>Foydalanuvchidan check:

👮‍♂️ Foydalanuvchi:</b> <a href='https://tg://user?id=$cid'>$name</a>
🔎 <b>ID raqami:</b> $fid
💵 <b>To'lov miqdori:</b> $hisob $pul",
'disable_web_page_preview'=>true,
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"✅ Tasdiqlash",'callback_data'=>"on=$fid"],['text'=>"❌ Bekor qilish",'callback_data'=>"off=$fid"]],
]])
]);
}}

if(mb_stripos($data,"on=")!==false){
$odam=explode("=",$data)[1];
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
$hisob=file_get_contents("step/hisob.$odam");
bot('SendMessage',[
'chat_id'=>$odam,
'text'=>"<b>✅ So'rovingiz qabul qilindi!</b>

Hisobingizga $hisob $pul qo'shildi",
'parse_mode'=>'html',
]);
bot('sendMessage',[
'chat_id'=>$yangi,
'text'=>"<b>🔹 Foydalanuvchi: <u>$odam</u> hisobini $hisob $pul'ga to'ldirdi!</b>",
'parse_mode'=>'html',
"reply_markup"=>json_encode([
'inline_keyboard'=>[
[['text'=>"🔹 Foydalanuvchi",'url'=>"tg://user?id=$odam"]],
]])
]);
$currency = file_get_contents("kabinet/$odam.dpz");
$get = file_get_contents("kabinet/$odam.som");
$get += $hisob;
$currency += $hisob;
file_put_contents("kabinet/$odam.som",$get);
file_put_contents("kabinet/$odam.dpz",$currency);
bot('SendMessage',[
'chat_id'=>$builder24,
'text'=>"<b>✅ Foydalanuvchi cheki qabul qilindi!</b>",
'parse_mode'=>'html',
]);
unlink("step/hisob.$odam");
}

if(mb_stripos($data,"off=")!==false){
$odam=explode("=",$data)[1];
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
$hisob=file_get_contents("step/hisob.$odam");
bot('SendMessage',[
'chat_id'=>$odam,
'text'=>"<b>❌ So'rovingiz bekor qilindi!</b>",
'parse_mode'=>'html',
]);
bot('SendMessage',[
'chat_id'=>$builder24,
'text'=>"<b>❌ Foydalanuvchi cheki bekor qilindi!</b>",
'parse_mode'=>'html',
]);
unlink("step/hisob.$odam");
}

if($data == "otqazma"){
bot('DeleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>📝 Kerakli foydalanuvchi IDsini yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"◀️ Orqaga"]]
]])
]);
file_put_contents("step/$cid.txt","otkazma");
exit();
}

if($userstep == "otkazma"){
if($text=="◀️ Orqaga"){
unlink("step/$cid.txt");
}else{
$odam=file_get_contents("kabinet/$text.som");
if($odam != null){
if($cid==$text){
bot("sendMessage",[
"chat_id"=>$cid,
"text"=>"<b>⚠️ O'zingizga pul o'tkaza olmaysiz!</b>",
'parse_mode'=>'html',
]);
exit();
}else{
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"📝 <b>O'tkazma uchun miqdorni yuboring:

Balans:</b> $som so'm (2% komissiya)",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"◀️ Orqaga"]]
]])
]);
file_put_contents("step/$cid.txt","otkazma2-$text");
exit();
}}else{
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Ushbu foydalanuvchi botdan foydalanmaydi!</b>

Qayta yuboring:",
'parse_mode'=>'html',
]);
exit();
}}}

if(mb_stripos($userstep, "otkazma2-")!==false){
if($text=="◀️ Orqaga"){
unlink("step/$cid.txt");
}else{
$ex = explode("-",$userstep);
$odam = $ex[1];
$plus = file_get_contents("kabinet/$odam.som");
$minus=file_get_contents("kabinet/$cid.som");
$komisa = $text - $text/100*2;
if($minus>=$komisa){
$qow = $plus + $komisa;
$ayr = $minus - $text;
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>✅ Muvaffaqiyatli amalga oshirildi!</b>

Foydalanuvchi hisobiga $komisa so'm o'tkazildi",
'parse_mode'=>'html',
'reply_markup'=>$menyu,
]);
file_put_contents("kabinet/$cid.som","$ayr");
bot("sendMessage",[
"chat_id"=>$odam,
"text"=>"<b>🔄 Hurmatli mijoz sizga pul o'tkazildi!</b>

Asosiy hisobingizga $komisa so'm qo'shildi",
'parse_mode'=>'html',
]);
file_put_contents("kabinet/$odam.som","$qow");
unlink("step/$cid.txt");
exit();
}else{
bot("sendMessage",[
"chat_id"=>$cid,
"text"=>"<b>⚠️ Mablag' yetarli emas!</b>",
'parse_mode'=>'html',
]);
exit();
}}}

if($data == "ishlash"){
bot('DeleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendmessage',[
'chat_id'=>$ccid,
'text'=>"<b>🔗 Sizning referal havolangiz:</b>

<code>https://t.me/$botname?start=$ccid</code>

<b>Sizga har bir taklif qilgan do'stingiz balansini to'ldirganda pulining 3% miqdori taqdim etiladi!</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"↗️ Ulashish",'url'=>"https://t.me/share/url?url=https://t.me/$botname?start=$ccid"]]
]])
]);
exit();
}

if($tx=="$tugma4"){
$subs = substr_count($stat,"\n");
$sana=file_get_contents("stat/date.txt");
$kun=file_get_contents("stat/day.txt");
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>@$botname - Loyiha statistikasi:

👥 Aktiv foydalanuvchilar:</b> $subs ta
<b>📈 Kiritilgan sarmoyalar:</b> $sid ta
<b>📥 Kiritilgan pullar:</b> $krt so'm
<b>📤 To'langan pullar:</b> $ych so'm
<b>📆 Botimiz ishlamoqda:</b> $kun kun

<b>🕐 Bot ishga tushgan sana: $sana</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"🥇 Investorlar(TOP)",'callback_data'=>"investor"]],
[['text'=>"🤖 Bot ochish",'url'=>"https://t.me/bot_yasovchi_robot"]],
[['text'=>"☎️ Adminstrator",'url'=>"tg://user?id=$builder24"]],
]])
]);
exit();
}

if($tx=="$tugma3"){
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Quyidagilardan birini tanlang</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"📎 Taklif",'callback_data'=>"ref"]],
]])
]);
exit();
}

if($data=="ref"){
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>🔗 Sizning referal havolangiz:</b>

<code>https://t.me/$botname?start=$ccid</code>

<b>Sizga har bir taklif qilgan do'stingiz uchun $taklifnarx $valyuta taqdim etiladi!</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"↗️ Ulashish",'url'=>"https://t.me/share/url?url=https://t.me/$botname?start=$ccid"]]
]])
]);
}

if($data=="malumot"){
$subs = substr_count($stat,"\n");
$sana=file_get_contents("stat/date.txt");
$kun=file_get_contents("stat/day.txt");
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>@$botname - Loyiha statistikasi:

👥 Aktiv foydalanuvchilar:</b> $subs ta
<b>📈 Kiritilgan sarmoyalar:</b> $sid ta
<b>📥 Kiritilgan pullar:</b> $krt so'm
<b>📤 To'langan pullar:</b> $ych so'm
<b>📆 Botimiz ishlamoqda:</b> $kun kun

<b>🕐 Bot ishga tushgan sana: $sana</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"🥇 Investorlar(TOP)",'callback_data'=>"investor"]],
[['text'=>"🤖 Bot ochish",'url'=>"https://t.me/MrUzbekDev"]],
[['text'=>"☎️ Adminstrator",'url'=>"tg://user?id=$builder24"]],

]])
]);
}

if($data =="investor"){
$daten = [];
$rev = [];
$fayllar = glob("kabinet/*.*");
foreach($fayllar as $file){
if(mb_stripos($file,".dpz")!==false){
$value = file_get_contents($file);
$id = str_replace(["kabinet/",".dpz"],["",""],$file);
$daten[$value] = $id;
$rev[$id] = $value;
}
echo $file;
}
asort($rev);
$reversed = array_reverse($rev);
for($i=0;$i<10;$i+=1){
$order = $i+1;
$id = $daten["$reversed[$i]"];
$text.= "<b>{$order}</b>. <a href='tg://user?id={$id}'>{$id}</a> - "."<code>".$reversed[$i]."</code>"." <b>so'm</b>"."\n";
}
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>🏆 TOP10 - Investorlarimiz:</b>

$text",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"malumot"]],
]])
]);
}

if($data =="kabinet"){
$daten = [];
$rev = [];
$fayllar = glob("kabinet/*.*");
foreach($fayllar as $file){
if(mb_stripos($file,".som")!==false){
$value = file_get_contents($file);
$id = str_replace(["kabinet/",".som"],["",""],$file);
$daten[$value] = $id;
$rev[$id] = $value;
}
echo $file;
}
asort($rev);
$reversed = array_reverse($rev);
for($i=0;$i<10;$i+=1){
$order = $i+1;
$id = $daten["$reversed[$i]"];
$text.= "<b>{$order}</b>. <a href='tg://user?id={$id}'>{$id}</a> - "."<code>".$reversed[$i]."</code>"." <b>so'm</b>"."\n";
}
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>🏆 TOP10 - Hisobdorlar:</b>

$text",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"malumot"]],
]])
]);
}

if($tx=="$tugma5"){
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>📝 Murojaat matnini yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"◀️ Orqaga"]],
]])
]);
file_put_contents("step/$cid.txt","suport");
exit();
}

if($userstep=="suport"){
if($tx=="◀️ Orqaga"){
unlink("step/$cid.txt");
}else{
bot('sendMessage',[
'chat_id'=>$builder24,
'text'=>"<b>📨 Yangi murojat keldi:</b> <a href='tg://user?id=$cid'>$cid</a>

<b>📑 Murojat matni:</b> $tx",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"Javob yozish",'callback_data'=>"yozish=$cid"]],
]])
]);
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>✅ Murojaatingiz yuborildi.</b>

Tez orada javob qaytaramiz!",
'parse_mode'=>'html',
'reply_markup'=>$menyu,
]);
unlink("step/$cid.txt");
exit();
}}

if(mb_stripos($data,"yozish=")!==false){
$odam=explode("=",$data)[1];
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"⏱ <b>Yuklanmoqda...</b>",
'parse_mode'=>'html',
]);
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"⏱ <b>Yuklanmoqda...</b>",
'parse_mode'=>'html',
]);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Javob matnini yuboring:</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"◀️ Orqaga"]],
]])
]);
file_put_contents("step/$ccid.txt","otvet=$odam");
exit();
}

if(mb_stripos($userstep, "otvet=")!==false){
$ex = explode("=",$userstep);
$odam = $ex[1];
if($tx=="◀️ Orqaga"){
unlink("step/$cid.txt");
}else{
bot('sendMessage',[
'chat_id'=>$odam,
'text'=>"<b>💌 Admindan xabar keldi:</b>

$tx",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"Javob yozish",'callback_data'=>"boglanish"]],
]])
]);
bot('sendMessage',[
'chat_id'=>$builder24,
'text'=>"<b>Javob yuborildi</b>",
'parse_mode'=>"html",
'reply_markup'=>$menyu,
]);
unlink("step/$cid.txt");
exit();
}}

if($tx=="/panel" or $tx=="🗄 Boshqarish"){
if(in_array($cid,$admin)){
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>🗄 Boshqaruv paneliga xush kelibsiz!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
exit();
}}

if($tx=="/started"){
$sanasi = date('d-m-Y', strtotime('2 hour'));
if(in_array($cid,$admin)){
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>⏱ Bot $sanasi sanadan ishga tushdi!</b>",
'parse_mode'=>'html',
]);
file_put_contents("stat/date.txt",$sanasi);
file_put_contents("stat/day.txt","0");
exit();
}}

if($tx=="📊 Statistika" and in_array($cid,$admin)){
$odam=substr_count($stat,"\n");
$ishda=file_get_contents("stat/day.txt");
$load = sys_getloadavg();
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>💡 O'rtacha yuklanish:</b> <code>$load[0]</code>

◾️ <b>Aktiv obunachilar:</b> $odam ta
<b>▫️ Barcha sarmoyalar:</b> $sid ta
<b>▫️ Botimiz ishlamoqda:</b> $ishda kun",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"🏆 Depozit",'callback_data'=>"investors"],['text'=>"🏆 Hisob",'callback_data'=>"hisobdors"]],
[['text'=>"🔁 Yangilash",'callback_data'=>"stats"]],
]])
]);
exit();
}

if($data=="stats"){
$odam=substr_count($stat,"\n");
$ishda=file_get_contents("stat/day.txt");
$load = sys_getloadavg();
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>💡 O'rtacha yuklanish:</b> <code>$load[0]</code>

◾️ <b>Aktiv obunachilar:</b> $odam ta
<b>▫️ Barcha sarmoyalar:</b> $sid ta
<b>▫️ Botimiz ishlamoqda:</b> $ishda kun",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"🏆 Depozit",'callback_data'=>"investors"],['text'=>"🏆 Hisob",'callback_data'=>"hisobdors"]],
[['text'=>"🔁 Yangilash",'callback_data'=>"stats"]],
]])
]);
exit();
}

if($data =="investors"){
$daten = [];
$rev = [];
$fayllar = glob("kabinet/*.*");
foreach($fayllar as $file){
if(mb_stripos($file,".dpz")!==false){
$value = file_get_contents($file);
$id = str_replace(["kabinet/",".dpz"],["",""],$file);
$daten[$value] = $id;
$rev[$id] = $value;
}
echo $file;
}
asort($rev);
$reversed = array_reverse($rev);
for($i=0;$i<10;$i+=1){
$order = $i+1;
$id = $daten["$reversed[$i]"];
$text.= "<b>{$order}</b>. <a href='tg://user?id={$id}'>{$id}</a> - "."<code>".$reversed[$i]."</code>"." <b>so'm</b>"."\n";
}
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>🏆 TOP10 - Investorlar:</b>

$text",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"stats"]],
]])
]);
}

if($data =="hisobdors"){
$daten = [];
$rev = [];
$fayllar = glob("kabinet/*.*");
foreach($fayllar as $file){
if(mb_stripos($file,".som")!==false){
$value = file_get_contents($file);
$id = str_replace(["kabinet/",".som"],["",""],$file);
$daten[$value] = $id;
$rev[$id] = $value;
}
echo $file;
}
asort($rev);
$reversed = array_reverse($rev);
for($i=0;$i<10;$i+=1){
$order = $i+1;
$id = $daten["$reversed[$i]"];
$text.= "<b>{$order}</b>. <a href='tg://user?id={$id}'>{$id}</a> - "."<code>".$reversed[$i]."</code>"." <b>so'm</b>"."\n";
}
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>🏆 TOP10 - Hisobdorlar:</b>

$text",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"stats"]],
]])
]);
}

//Investiya

if($text=="📈 Investitsiya" and in_array($cid,$admin)){
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>📈 Investitsiya sozlamalari bo'limidasiz!</b>

Nimani o'zgartiramiz?",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"➕ Tarif qo'shish",'callback_data'=>"tarif_qosh"]],
[['text'=>"⚙ Tarif sozlash",'callback_data'=>"tarif_soz"]],
]])
]);
exit();
}

if($data =="invest"){
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>📈 Investitsiya sozlamalari bo'limidasiz!</b>

Nimani o'zgartiramiz?",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"➕ Tarif qo'shish",'callback_data'=>"tarif_qosh"]],
[['text'=>"⚙ Tarif sozlash",'callback_data'=>"tarif_soz"]],
]])
]);
}

if($data =="tarif_qosh"){
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>➕ Tarif qo'shish uchun kategoriya tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"Kunlik daromad",'callback_data'=>"kunlik_qosh"],['text'=>"Standard daromad",'callback_data'=>"standard_qosh"]],
[['text'=>"◀️ Orqaga",'callback_data'=>"invest"]],
]])
]);
}

if($data =="tarif_soz"){
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>⚙ Tarif sozlash uchun kategoriya tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"Kunlik daromad",'callback_data'=>"kunlik_soz"],['text'=>"Standard daromad",'callback_data'=>"standard_soz"]],
[['text'=>"◀️ Orqaga",'callback_data'=>"invest"]],
]])
]);
}

if($data=="kunlik_soz"){
$tarif=file_get_contents("tarif/kunlik.txt");
if($tarif == null){
bot('answerCallbackQuery',[
'callback_query_id'=>$callid,
'text'=>"🤷🏻‍♂ Hech qanday tariflar topilmadi!",
'show_alert'=>true,
]);
}else{
$s=explode("\n",$tarif);
$soni = substr_count($tarif,"\n");
$key=[];
for($i=1;$i<=$soni;$i++){
$tikpul=file_get_contents("tarif/".$s[$i]."/krt.pul");
$kunpul=file_get_contents("tarif/".$s[$i]."/kun.pul");
$kun=file_get_contents("tarif/".$s[$i]."/ish.kun");
$umumiy=$kunpul*$kun;
$key[]=["text"=>"$tikpul so'm -> $umumiy so'm ($kun kun)","callback_data"=>"kundrsoz=".$s[$i]];
}
$keysboard2 = array_chunk($key, 1);
$keysboard2[] = [['text'=>"◀️ Orqaga",'callback_data'=>"tarif_soz"]];
$tariflar = json_encode([
'inline_keyboard'=>$keysboard2,
]);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>⬇️ Quyidagi tarflardan birini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>$tariflar
]);
exit();
}}

if(mb_stripos($data, "kundrsoz=")!==false){
$ex = explode("=",$data);
$tarif = $ex[1];
$krt = file_get_contents("tarif/$tarif/krt.pul");
$kdr = file_get_contents("tarif/$tarif/kun.pul");
$kun = file_get_contents("tarif/$tarif/ish.kun");
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"💰 <b>Tarif nomi: <u>$tarif</u></b>

▫️ <b>Sarmoya narxi:</b> $krt so'm
▫️ <b>Kunlik daromad:</b> $kdr so'm
▫️ <b>Ishlash kuni:</b> $kun kun

Sozlash uchun quyidagilardan foydalaning!",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"Ishlash kuni",'callback_data'=>"sozlash=$tarif=ish.kun"]],
[['text'=>"Sarmoya narxi",'callback_data'=>"sozlash=$tarif=krt.pul"],['text'=>"Kunlik daromad",'callback_data'=>"sozlash=$tarif=kun.pul"]],
[['text'=>"🗑 O'chirish",'callback_data'=>"delete1=$tarif"],['text'=>"◀️ Orqaga",'callback_data'=>"kunlik_soz"]],
]])
]);
}

if($data=="standard_soz"){
$tarif = file_get_contents("tarif/standard.txt");
if($tarif == null){
bot('answerCallbackQuery',[
'callback_query_id'=>$callid,
'text'=>"🤷🏻‍♂ Hech qanday tariflar topilmadi!",
'show_alert'=>true,
]);
}else{
$s=explode("\n",$tarif);
$soni = substr_count($tarif,"\n");
$key=[];
for($i=1;$i<=$soni;$i++){
$krt=file_get_contents("tarif/".$s[$i]."/krt.pul");
$oln=file_get_contents("tarif/".$s[$i]."/oln.pul");
$kun=file_get_contents("tarif/".$s[$i]."/ish.kun");
$key[]=["text"=>"$krt so'm -> $oln so'm ($kun kun)","callback_data"=>"standrsoz=".$s[$i]];
}
$keysboard2 = array_chunk($key, 1);
$keysboard2[] = [['text'=>"◀️ Orqaga",'callback_data'=>"tarif_soz"]];
$tariflar = json_encode([
'inline_keyboard'=>$keysboard2,
]);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"<b>⬇️ Quyidagi tarflardan birini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>$tariflar
]);
exit();
}}

if(mb_stripos($data, "standrsoz=")!==false){
$ex = explode("=",$data);
$tarif = $ex[1];
$krt = file_get_contents("tarif/$tarif/krt.pul");
$oln = file_get_contents("tarif/$tarif/oln.pul");
$kun = file_get_contents("tarif/$tarif/ish.kun");
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"💰 <b>Tarif nomi: <u>$tarif</u></b>

▫️ <b>Sarmoya narxi:</b> $krt so'm
▫️ <b>Jami daromad:</b> $oln so'm
▫️ <b>Ishlash kuni:</b> $kun kun

Sozlash uchun quyidagilardan foydalaning!",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"Ishlash kuni",'callback_data'=>"sozlash=$tarif=ish.kun"]],
[['text'=>"Sarmoya narxi",'callback_data'=>"sozlash=$tarif=krt.pul"],['text'=>"Sarmoya daromad",'callback_data'=>"sozlash=$tarif=oln.pul"]],
[['text'=>"🗑 O'chirish",'callback_data'=>"delete2=$tarif"],['text'=>"◀️ Orqaga",'callback_data'=>"standard_soz"]],
]])
]);
}

if(mb_stripos($data, "delete1=")!==false){
$ex = explode("=",$data);
$tarif = $ex[1];
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
$info=file_get_contents("tarif/kunlik.txt");
$del = str_replace("\n".$tarif."","",$info);
file_put_contents("tarif/kunlik.txt",$del);
deleteFolder("tarif/$tarif");
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Muvaffaqiyatli o'chirildi!</b>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
exit();
}

if(mb_stripos($data, "delete2=")!==false){
$ex = explode("=",$data);
$tarif = $ex[1];
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
$info=file_get_contents("tarif/standard.txt");
$del = str_replace("\n".$tarif."","",$info);
file_put_contents("tarif/standard.txt",$del);
deleteFolder("tarif/$tarif");
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Muvaffaqiyatli o'chirildi!</b>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
exit();
}

if(mb_stripos($data, "sozlash=")!==false){
$ex = explode("=",$data);
$tarif = $ex[1];
$file = $ex[2];
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>📝 Yangi qiymatni yuboring:</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqaruv"]],
]])
]);
file_put_contents("step/$ccid.txt","sozlash=$tarif=$file");
exit();
}

if(mb_stripos($userstep, "sozlash=")!==false){
$ex = explode("=",$userstep);
$tarif = $ex[1];
$file = $ex[2];
if($tx=="🗄 Boshqaruv"){
unlink("step/$cid.txt");
}else{
file_put_contents("tarif/$tarif/$file","$tx");
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Muvaffaqiyatli o'zgartirildi!</b>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
unlink("step/$cid.txt");
exit();
}}

if($data=="kunlik_qosh"){
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>📝 Tarif uchun nom yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$ccid.txt","kunliknom");
}

if($userstep=="kunliknom"){
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>📝 Tarif uchun narxni yuboring:</b>",
'parse_mode'=>'html',
]);
file_put_contents("step/$cid.txt","kunliknarx-$text");
exit();
}}

if(mb_stripos($userstep, "kunliknarx-")!==false){
$ex = explode("-",$userstep);
$tarif = $ex[1];
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>📝 Kunlik daromad miqdorini yuboring:</b>",
'parse_mode'=>'html',
]);
file_put_contents("step/$cid.txt","kundr-$tarif-$text");
exit();
}}

if(mb_stripos($userstep, "kundr-")!==false){
$ex = explode("-",$userstep);
$tarif = $ex[1];
$narx = $ex[2];
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>📝 Tarifning ishlash kunini yuboring:</b>",
'parse_mode'=>'html',
]);
file_put_contents("step/$cid.txt","kunlikkun-$tarif-$narx-$text");
exit();
}}

if(mb_stripos($userstep, "kunlikkun-")!==false){
$ex = explode("-",$userstep);
$tarif = $ex[1];
$narx = $ex[2];
$kundr = $ex[3];
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
$qow=file_get_contents("tarif/kunlik.txt");
file_put_contents("tarif/kunlik.txt","$qow\n$tarif");
mkdir("tarif/$tarif");
file_put_contents("tarif/$tarif/krt.pul", $narx);
file_put_contents("tarif/$tarif/kun.pul",$kundr);
file_put_contents("tarif/$tarif/ish.kun",$text);
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>✅ $tarif muvaffaqiyatli qo'shildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("step/$cid.txt");
exit();
}}

if($data=="standard_qosh"){
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>📝 Tarif uchun nom yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$ccid.txt","stannom");
}

if($userstep=="stannom"){
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>📝 Tarif uchun narxni yuboring:</b>",
'parse_mode'=>'html',
]);
file_put_contents("step/$cid.txt","stannarx-$text");
exit();
}}

if(mb_stripos($userstep, "stannarx-")!==false){
$ex = explode("-",$userstep);
$tarif = $ex[1];
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>📝 Umumiy daromad miqdorini yuboring:</b>",
'parse_mode'=>'html',
]);
file_put_contents("step/$cid.txt","standr-$tarif-$text");
exit();
}}

if(mb_stripos($userstep, "standr-")!==false){
$ex = explode("-",$userstep);
$tarif = $ex[1];
$narx = $ex[2];
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>📝 Tarifning ishlash kunini yuboring:</b>",
'parse_mode'=>'html',
]);
file_put_contents("step/$cid.txt","stankun-$tarif-$narx-$text");
exit();
}}

if(mb_stripos($userstep, "stankun-")!==false){
$ex = explode("-",$userstep);
$tarif = $ex[1];
$narx = $ex[2];
$standr = $ex[3];
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
$qow=file_get_contents("tarif/standard.txt");
file_put_contents("tarif/standard.txt","$qow\n$tarif");
mkdir("tarif/$tarif");
file_put_contents("tarif/$tarif/krt.pul", $narx);
file_put_contents("tarif/$tarif/oln.pul",$standr);
file_put_contents("tarif/$tarif/ish.kun",$text);
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>✅ $tarif muvaffaqiyatli qo'shildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("step/$cid.txt");
exit();
}}

//search

if($tx=="🔎 Foydalanuvchini boshqarish" and in_array($cid,$admin)){
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Kerakli foydalanuvchining ID raqamini yuboring:</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$cid.txt","idraqam");
exit();
}

if($userstep=="idraqam"){
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
if(file_exists("kabinet/$tx.som")){
$som=file_get_contents("kabinet/$tx.som");
$dpz=file_get_contents("kabinet/$tx.dpz");
$ban = file_get_contents("ban/$text.txt");
if($ban == null){
$bn = "🔔 Ban qilish";
}
if($ban == "ban"){
$bn = "🔕 Bandan olish";
}
bot("sendMessage",[
"chat_id"=>$cid,
"text"=>"<b>┌👤 Foydalanuvchi topildi!
├
├Balans:</b> $som so'm
<b>├Depozit:</b> $dpz so'm
├
<b>└@$botname - Yuqori daromad!</b>",
'parse_mode'=>"html",
"reply_markup"=>json_encode([
'inline_keyboard'=>[
[['text'=>"$bn",'callback_data'=>"ban=$tx"]],
[['text'=>"➕ Pul qo'shish",'callback_data'=>"qoshish=$tx"],['text'=>"➖ Pul ayirish",'callback_data'=>"ayirish=$tx"]],
]])
]); 
unlink("step/$cid.txt");
exit();
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Ushbu foydalanuvchi botdan foydalanmaydi!</b>",
'parse_mode'=>'html',
]);
exit();
}}}

if(mb_stripos($data, "ban=")!==false){
$ex = explode("=",$data);
$odam = $ex[1];
$ban = file_get_contents("ban/$odam.txt");
if($builder24 != $odam){
if($ban == "ban"){
unlink("ban/$odam.txt");
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Foydalanuvchi bandan olindi!</b>",
'parse_mode'=>"html",
]);
bot('sendMessage',[
'chat_id'=>$odam,
'text'=>"<b>Admin tomonidan bandan olindingiz!</b>",
'parse_mode'=>"html",
]);
exit();
}else{
file_put_contents("ban/$odam.txt",'ban');
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Foydalanuvchi banlandi!</b>",
'parse_mode'=>"html",
]);
bot('sendMessage',[
'chat_id'=>$odam,
'text'=>"<b>Admin tomonidan ban oldingiz!</b>",
'parse_mode'=>"html",
]);
exit();
}}else{
bot('answerCallbackQuery',[
'callback_query_id'=>$callid,
'text'=>"Asosiy adminni bloklash mumkin emas!",
'show_alert'=>true,
]);
}}

if(mb_stripos($data, "qoshish=")!==false){
$ex = explode("=",$data);
$odam = $ex[1];
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'parse_mode'=>"html",
'text'=>"<b>[$odam]ning hisobiga qancha pul qo'shmoqchisiz?</b>",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$ccid.txt","qoshish=$odam");
exit();
}

if(mb_stripos($userstep, "qoshish=")!==false){
$ex = explode("=",$userstep);
$odam = $ex[1];
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
$som=file_get_contents("kabinet/$odam.som");
$som += $tx;
file_put_contents("kabinet/$odam.som", $som);
$dpz=file_get_contents("kabinet/$odam.dpz");
$dpz += $tx;
file_put_contents("kabinet/$odam.dpz",$dpz);
bot('sendMessage',[
'chat_id'=>$odam,
'text'=>"<b>Admin tomonidan hisobingiz $tx so'm to'ldirildi!</b>",
'parse_mode'=>"html",
]);
bot('sendMessage',[
'chat_id'=>"$news",
'text'=>"<b>📤 Foydalanuvchi hisobini to'ldirdi!</b>

<b>▫️ Foydalanuvchi:</b> <a href='tg://user?id=$odam'>$odam</a>
<b>▫️ Summa:</b> $tx so'm 

<b>@$botname - Yuqori daromad!</b>",
'parse_mode'=>'html',
"reply_markup"=>json_encode([
'inline_keyboard'=>[
[['text'=>"🤖",'url'=>"https://t.me/$botname"]],
]])
]);
$caw = file_get_contents("kabinet/$odam.txt");
$tkf = file_get_contents("kabinet/$caw.som");
$plus3 = $tx/100*3 + $tkf;
bot('SendMessage',[
'chat_id'=>$caw,
'text'=>"<b>📳 Do'stingiz hisobini to'ldirgani uchun sizga $plus3 so'm qo'shildi!</b>",
'parse_mode'=>'html',
]);
file_put_contents("kabinet/$caw.som",$plus3);
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Foydalanuvchi hisobiga $tx so'm qo'shildi</b>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
$krt = file_get_contents("stat/kirit.txt");
$plus4 = $krt + $tx;
file_put_contents("stat/kirit.txt",$plus4);
unlink("step/$cid.txt");
exit();
}}

if(mb_stripos($data, "ayirish=")!==false){
$ex = explode("=",$data);
$odam = $ex[1];
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'parse_mode'=>"html",
'text'=>"<b>[$odam]ning hisobidan qancha pul ayirmoqchisiz?</b>",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$ccid.txt","ayirish=$odam");
exit();
}

if(mb_stripos($userstep, "ayirish=")!==false){
$ex = explode("=",$userstep);
$odam = $ex[1];
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
bot('sendMessage',[
'chat_id'=>$odam,
'text'=>"<b>Admin tomonidan hisobingizdan $tx so'm olib tashlandi!</b>",
'parse_mode'=>"html",
]);
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Foydalanuvchi hisobidan $tx so'm olib tashlandi</b>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
$som=file_get_contents("kabinet/$odam.som");
$som -= $tx;
file_put_contents("kabinet/$odam.som", $som);
$dpz=file_get_contents("kabinet/$odam.dpz");
$dpz -= $tx;
file_put_contents("kabinet/$odam.dpz", $dpz);
unlink("step/$cid.txt");
exit();
}}

//Xabar funksiyasi

if($tx=="📩 Xabarnoma" and in_array($cid,$admin)){
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>📨 Yuboriladigan xabar turini tanlang:</b>",
'parse_mode'=>"html",
'reply_markup'=> json_encode([
'inline_keyboard'=>[
[['text'=>"Oddiy xabar",'callback_data'=>"oddiy_xabar"],['text'=>"Forward xabar",'callback_data'=>"forward_xabar"]],
[['text'=>"Foydalanuvchiga xabar",'callback_data'=>"obuna_xabar"]],
]])
]);
exit();
}


if($data=="oddiy_xabar" and in_array($ccid,$admin)){
$odam=substr_count($stat,"\n");
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>{$odam}ta foydalanuvchiga yuboriladigan xabar matnini yuboring:</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$ccid.txt","oddiy");
exit();
}
if($userstep=="oddiy"){
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>Xabar yuborish boshlandi!</b>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
$odam = explode("\n",$stat);
foreach($odam as $odamlar){
$usr=bot("sendMessage",[
'chat_id'=>$odamlar,
'text'=>$text,
'parse_mode'=>'HTML'
]);
exit();
}}}
if($usr){
$odam=substr_count($stat,"\n");
bot("sendmessage",[
'chat_id'=>$cid,
'text'=>"<b>{$odam}ta foydalanuvchiga muvaffaqiyatli yuborildi</b>",
'parse_mode'=>'html',
]);
unlink("step/$cid.txt");
exit();
}

if($data =="forward_xabar" and in_array($ccid,$admin)){
$odam=substr_count($stat,"\n");
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>{$odam}ta foydalanuvchiga yuboriladigan xabarni forward shaklida yuboring:</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$ccid.txt","forward");
exit();
}
if($userstep=="forward"){
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>Xabar yuborish boshlandi!</b>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
$odam = explode("\n",$stat);
foreach($odam as $odamlar){
$fors=bot("forwardMessage",[
'from_chat_id'=>$cid,
'chat_id'=>$odamlar,
'message_id'=>$mid,
]);
exit();
}}}
if($fors){
$odam=substr_count($stat,"\n");
bot("sendmessage",[
'chat_id'=>$cid,
'text'=>"<b>{$odam}ta foydalanuvchiga muvaffaqiyatli yuborildi</b>",
'parse_mode'=>'html',
]);
unlink("step/$cid.txt");
exit();
}

if($data =="obuna_xabar" and in_array($ccid,$admin)){
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Kerakli foydalanuvchi ID raqamini yuboring:</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$ccid.txt","odamtop");
exit();
}

if($userstep=="odamtop"){
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
if(mb_stripos($stat,"$text")!==false){
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Foydalanuvchi topildi, yuboriladigan xabarni kiriting:</b>",
'parse_mode'=>"html",
]);
file_put_contents("step/$ccid.txt","yubor=$text");
exit();
}else{
bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>Ushbu foydalanuvchi botdan foydalanmaydi!</b>",
'parse_mode'=>"html",
]);
exit();
}}}

if(mb_stripos($userstep, "yubor=")!==false){
$ex = explode("=",$userstep);
$odam = $ex[1];
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>Xabar yuborildi!</b>",
'parse_mode'=>"html",
'reply_markup'=>$admin1_menu,
]);
unlink("step/$cid.txt");
bot('sendmessage',[
'chat_id'=>$odam,
'text'=>"<b>☎️ Adminstrator:</b> $text",
'parse_mode'=>"html",
]);
exit();
}}

//Tugmalar

if($tx=="🎛 Tugmalar" and in_array($cid,$admin)){
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<i>Nimani o'zgartiramiz?</i>",
'parse_mode'=>"html",
'reply_markup'=> json_encode([
'inline_keyboard'=>[
[['text'=>"$tugma1",'callback_data'=>"tugmatah-tugma1"]],
[['text'=>"$tugma2",'callback_data'=>"tugmatah-tugma2"],['text'=>"$tugma3",'callback_data'=>"tugmatah-tugma3"]],
[['text'=>"$tugma4",'callback_data'=>"tugmatah-tugma4"],['text'=>"$tugma5",'callback_data'=>"tugmatah-tugma5"]],
[['text'=>"⚠️ Avvalgisiga qaytarish",'callback_data'=>"reset_tugma"]],
]])
]);
}

if(mb_stripos($data, "tugmatah-")!==false){
$ex = explode("-",$data)[1];
$holat = file_get_contents("tugma/$ex.txt");
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Hozirgi holat:</b> $holat

<i>Yangi qiymatni yuboring:</i>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$ccid.txt","tugmath-$ex");
}

if(mb_stripos($userstep, "tugmath-")!==false){
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
if(isset($text)){
$ex = explode("-",$userstep)[1];
file_put_contents("tugma/$ex.txt",$text);
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Muvaffaqiyatli o'zgartirildi.</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("step/$cid.txt");
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>⚠️ Faqat harflardan foydalaning!</b>",
'parse_mode'=>'html',
]);
}}}

if($data=="reset_tugma"){
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"⏱ <b>Yuklanmoqda...</b>",
'parse_mode'=>"html",
]);
sleep(0.7);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Tugma nomlari o'z holiga qaytarildi!</b>",
'parse_mode'=>"html",
]);
deleteFolder("tugma/");
}

//Matnlar

if($tx=="📑 Matnlar" and in_array($cid,$admin)){
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<i>Nimani o'zgartiramiz?</i>",
'parse_mode'=>"html",
'reply_markup'=> json_encode([
'inline_keyboard'=>[
[['text'=>"Boshlangʻich matn",'callback_data'=>"matntah-bosh"]],
[['text'=>"Referal matn",'callback_data'=>"matntah-ref"],['text'=>"Investor matn",'callback_data'=>"matntah-inves"]],
[['text'=>"Maʼlumotdagi matn",'callback_data'=>"matntah-mal"],['text'=>"Kabinetdagi matn",'callback_data'=>"matntah-kab"]],
[['text'=>"⚠️ Avvalgisiga qaytarish",'callback_data'=>"reset_tugma"]],
]])
]);
}

if(mb_stripos($data, "matntah-")!==false){
$ex = explode("-",$data)[1];
$holat = file_get_contents("matn/$ex.txt");
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Hozirgi holat:</b> $holat

<i>Yangi qiymatni yuboring:</i>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]])
]);
file_put_contents("step/$ccid.txt","matn-$ex");
}

if(mb_stripos($userstep, "tugmath-")!==false){
if($tx=="🗄 Boshqarish"){
unlink("step/$cid.txt");
}else{
if(isset($text)){
$ex = explode("-",$userstep)[1];
file_put_contents("matn/$ex.txt",$text);
bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Muvaffaqiyatli o'zgartirildi.</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("step/$cid.txt");
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>⚠️ Faqat harflardan foydalaning!</b>",
'parse_mode'=>'html',
]);
}}}

if($data=="reset_matn"){
bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
'text'=>"⏱ <b>Yuklanmoqda...</b>",
'parse_mode'=>"html",
]);
sleep(0.7);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
]);
bot('sendMessage',[
'chat_id'=>$ccid,
'text'=>"<b>Matn nomlari o'z holiga qaytarildi!</b>",
'parse_mode'=>"html",
]);
deleteFolder("matn/");
}


?>
