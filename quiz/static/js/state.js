

var handles = ["SELECT STATE","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka",
                                        "Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab", "Rajasthan","Sikkim","Tamil Nadu",
                                        "Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Ladakh",
                                        "Chandigarh","Lakshadweep","Andaman and Nicobar Islands"];

$(function() {
  var options = '';
  for (var i = 0; i < handles.length; i++) {
      options += '<option value="' + handles[i] + '">' + handles[i] + '</option>';
  }
  $('#listBox').html(options);
});
function selct_district($val)
{
    if($val=='SELECT STATE') {
   var options = '';
  $('#secondlist').html(options);
  }
 if($val=='Andhra Pradesh') {
   var andhra = ['SELECT DISTRICT','Anantapur','Chittoor','East Godavari','Guntur','Kadapa','Krishna','Kurnool','Nellore',
   'Prakasam','Srikakulam','Visakhapatnam','Vizianagaram','West Godavari'];
   $(function() {
  var options = '';
  for (var i = 0; i < andhra.length; i++) {
      options += '<option value="' + andhra[i] + '">' + andhra[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Arunachal Pradesh') {
    var ap = ['SELECT DISTRICT','Anjaw','Central Siang','Changlang','Dibang Valley','East Kameng','East Siang','Kamle','Kra Daadi',
    'Kurung Kumey','Lepa Rada','Lohit','Longding','Lower Dibang Valley','Lower Siang','Lower Subansiri','Namsai',
    'Pakke Kessang','Papum Pare','Shi Yomi','Tawang','Tirap','Upper Siang','Upper Subansiri','West Kameng','West Siang'];
   $(function() {
  var options = '';
  for (var i = 0; i < ap.length; i++) {
      options += '<option value="' + ap[i] + '">' + ap[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Assam') {
    var assam = ['SELECT DISTRICT','Baksa','Barpeta','Biswanath','Bongaigaon','Cachar','Charaideo','Chirang','Darrang','Dhemaji','Dhubri',
    'Dibrugarh','Dima Hasao','Goalpara','Golaghat','Hailakandi','Hojai','Jorhat','Kamrup','Kamrup Metropolitan',
    'Karbi Anglong','Karimganj','Kokrajhar','Lakhimpur','Majuli','Morigaon','Nagaon','Nalbari','Sivasagar','Sonitpur',
    'South Salmara-Mankachar','Tinsukia','Udalguri','West Karbi Anglong'];
   $(function() {
  var options = '';
  for (var i = 0; i < assam.length; i++) {
      options += '<option value="' + assam[i] + '">' + assam[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Bihar') {
    var bihar = ['SELECT DISTRICT','Araria','Arwal','Aurangabad','Banka','Begusarai','Bhagalpur','Bhojpur','Buxar','Darbhanga','East Champaran','Gaya',
    'Gopalganj','Jamui','Jehanabad','Kaimur','Katihar','Khagaria','Kishanganj','Lakhisarai','Madhepura',
    'Madhubani','Munger','Muzaffarpur','Nalanda','Nawada','Patna','Purnia','Rohtas','Saharsa','Samastipur',
    'Saran','Sheikhpura','Sheohar','Sitamarhi','Siwan','Supaul','Vaishali','West Champaran'];
   $(function() {
  var options = '';
  for (var i = 0; i < bihar.length; i++) {
      options += '<option value="' + bihar[i] + '">' + bihar[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Chhattisgarh') {
    var Chhattisgarh = ['SELECT DISTRICT','Balod','Baloda Bazar','Balrampur','Bastar','Bemetara','Bijapur','Bilaspur','Dantewada','Dhamtari','Durg',
    'Gariaband','Gaurela Pendra Marwahi','Janjgir Champa','Jashpur','Kabirdham','Kanker',
    'Kondagaon','Korba','Koriya','Mahasamund','Mungeli','Narayanpur','Raigarh','Raipur','Rajnandgaon',
    'Sukma','Surajpur','Surguja'];
   $(function() {
  var options = '';
  for (var i = 0; i < Chhattisgarh.length; i++) {
      options += '<option value="' + Chhattisgarh[i] + '">' + Chhattisgarh[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Dadra and Nagar Haveli') {
    var dadra = ['SELECT DISTRICT','Dadra and Nagar Haveli'];
   $(function() {
  var options = '';
  for (var i = 0; i < dadra.length; i++) {
      options += '<option value="' + dadra[i] + '">' + dadra[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Daman and Diu') {
    var daman = ['SELECT DISTRICT',"Daman","Diu"];
   $(function() {
  var options = '';
  for (var i = 0; i < daman.length; i++) {
      options += '<option value="' + daman[i] + '">' + daman[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Delhi') {
    var delhi = ['SELECT DISTRICT','Central Delhi','East Delhi','New Delhi','North Delhi','North East Delhi','North West Delhi','Shahdara',
    'South Delhi','South East Delhi','South West Delhi','West Delhi'];
   $(function() {
  var options = '';
  for (var i = 0; i < delhi.length; i++) {
      options += '<option value="' + delhi[i] + '">' + delhi[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Goa') {
    var goa = ['SELECT DISTRICT','North Goa','South Goa'];
   $(function() {
  var options = '';
  for (var i = 0; i < goa.length; i++) {
      options += '<option value="' + goa[i] + '">' + goa[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Gujarat') {
    var gujarat = ['SELECT DISTRICT','Ahmedabad','Amreli','Anand','Aravalli','Banaskantha','Bharuch','Bhavnagar','Botad','Chhota Udaipur',
    'Dahod','Dang','Devbhoomi Dwarka','Gandhinagar','Gir Somnath','Jamnagar','Junagadh','Kheda','Kutch',
    'Mahisagar','Mehsana','Morbi','Narmada','Navsari','Panchmahal','Patan','Porbandar','Rajkot','Sabarkantha',
    'Surat','Surendranagar','Tapi','Vadodara','Valsad'];
   $(function() {
  var options = '';
  for (var i = 0; i < gujarat.length; i++) {
      options += '<option value="' + gujarat[i] + '">' + gujarat[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Haryana') {
    var haryana = ['SELECT DISTRICT','Ambala','Bhiwani','Charkhi Dadri','Faridabad','Fatehabad','Gurugram','Hisar','Jhajjar','Jind','Kaithal',
    'Karnal','Kurukshetra','Mahendragarh','Mewat','Palwal','Panchkula','Panipat','Rewari','Rohtak','Sirsa',
    'Sonipat','Yamunanagar'];
   $(function() {
  var options = '';
  for (var i = 0; i < haryana.length; i++) {
      options += '<option value="' + haryana[i] + '">' + haryana[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Himachal Pradesh') {
    var himachal = ['SELECT DISTRICT','Bilaspur','Chamba','Hamirpur','Kangra','Kinnaur','Kullu','Lahaul Spiti','Mandi','Shimla',
    'Sirmaur','Solan','Una'];
   $(function() {
  var options = '';
  for (var i = 0; i < himachal.length; i++) {
      options += '<option value="' + himachal[i] + '">' + himachal[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Jammu and Kashmir') {
    var jammu = ['SELECT DISTRICT','Anantnag','Bandipora','Baramulla','Budgam','Doda','Ganderbal','Jammu','Kathua','Kishtwar',
    'Kulgam','Kupwara','Poonch','Pulwama','Rajouri','Ramban','Reasi','Samba','Shopian','Srinagar',
    'Udhampur'];
   $(function() {
  var options = '';
  for (var i = 0; i < jammu.length; i++) {
      options += '<option value="' + jammu[i] + '">' + jammu[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Jharkhand') {
    var jharkhand = ['SELECT DISTRICT','Bokaro','Chatra','Deoghar','Dhanbad','Dumka','East Singhbhum','Garhwa','Giridih','Godda','Gumla','Hazaribagh',
    'Jamtara','Khunti','Koderma','Latehar','Lohardaga','Pakur','Palamu','Ramgarh','Ranchi','Sahebganj',
    'Seraikela Kharsawan','Simdega','West Singhbhum'];
   $(function() {
  var options = '';
  for (var i = 0; i < jharkhand.length; i++) {
      options += '<option value="' + jharkhand[i] + '">' + jharkhand[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Karnataka') {
    var karnataka = ['SELECT DISTRICT',"Bagalkot","Bangalore Urban","Bangalore Rural","Belgaum","Bellary","Bidar","Chamarajnagar", 
    "Chikkamagaluru","Chitradurga","Davanagere","Dharwad","Dakshina Kannada","Gadag",
    "Gulbarga","Hassan","Haveri","Kodagu","Kolar","Koppal","Mandya","Mysore","Raichur",
    "Shimoga","Tumkur","Udupi","Uttara Kannada","Ramanagara","Yadgir"];
   $(function() {
  var options = '';
  for (var i = 0; i < karnataka.length; i++) {
      options += '<option value="' + karnataka[i] + '">' + karnataka[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Kerala') {
    var kerala = ['SELECT DISTRICT',"Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam","Kottayam","Kozhikode","Malappuram",
    "Palakkad","Pathanamthitta","Thrissur","Thiruvananthapuram","Wayanad"];
   $(function() {
  var options = '';
  for (var i = 0; i < kerala.length; i++) {
      options += '<option value="' + kerala[i] + '">' + kerala[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Madhya Pradesh') {
    var mp =  ['SELECT DISTRICT',"Agar Malwa","Alirajpur","Anuppur","Ashoknagar","Balaghat","Barwani","Betul","Bhind","Bhopal",
    "Burhanpur","Chachaura","Chhatarpur","Chhindwara","Damoh","Datia","Dindori","Dewas","Dhar","Guna","Gwalior","Hoshangabad",
    "Indore","Jhabua","Jabalpur","Khandwa","Khargone","Maihar",
    "Mandla","Mandsaur","Morena","Narsinghpur","Neemuch"," Niwari","Nagda","Panna","Raisen","Ratlam","Rajgarh",
    "Rewa","Sagar","Satna","Sehore","Seoni","Shahdol","Shajapur","Sheopur","Shivpuri","Sidhi","Singrauli","Tikamgarh","Ujjain","Umaria","Vidisha"];
   $(function() {
  var options = '';
  for (var i = 0; i < mp.length; i++) {
      options += '<option value="' + mp[i] + '">' + mp[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Maharashtra') {
    var maharashtra =  ['SELECT DISTRICT', 'Ahmednagar', 'Akola', 'Amravati', 'Aurangabad', 'Beed', 'Bhandara', 'Buldhana', 'Chandrapur',
    'Dhule', 'Gadchiroli', 'Gondia', 'Hingoli', 'Jalgaon', 'Jalna', 'Kolhapur', 'Latur', 'Mumbai'
    ,'Nagpur','Nanded','Nandurbar','Nashik','Osmanabad','Palghar','Parbhani','Pune',
    'Raigad','Ratnagiri','Sangli','Satara','Sindhudurg','Solapur','Thane','Wardha','Washim','Yavatmal'];
   $(function() {
  var options = '';
  for (var i = 0; i < maharashtra.length; i++) {
      options += '<option value="' + maharashtra[i] + '">' + maharashtra[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
   if ($val=='Manipur') {
    var manipur =  ['SELECT DISTRICT',"Bishnupur","Churachandpur","Chandel","Imphal East","Imphal West","Jiribam","Kakching",
    "Kamjong","Kangpokpi","Noney","Pherzawl","Senapati","Tamenglong","Tengnoupal","Thoubal","Ukhrul" ];
   $(function() {
  var options = '';
  for (var i = 0; i < manipur.length; i++) {
      options += '<option value="' + manipur[i] + '">' + manipur[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
   if ($val=='Meghalaya') {
    var meghalaya =  ['SELECT DISTRICT',"East Garo Hills","East Jaintia Hills","East Khasi Hills","North Garo Hills","Ri Bhoi","South Garo Hills",
    "South West Garo Hills","South West Khasi Hills","West Garo Hills","West Jaintia Hills",
    "West Khasi Hills"];
   $(function() {
  var options = '';
  for (var i = 0; i < meghalaya.length; i++) {
      options += '<option value="' + meghalaya[i] + '">' + meghalaya[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
   if ($val=='Mizoram') {
    var mizoram = ['SELECT DISTRICT',"Aizawl","Champhai","Kolasib","Lawngtlai","Lunglei","Mamit","Saiha","Serchhip"];
   $(function() {
  var options = '';
  for (var i = 0; i < mizoram.length; i++) {
      options += '<option value="' + mizoram[i] + '">' + mizoram[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
   if ($val=='Nagaland') {
    var nagaland = ['SELECT DISTRICT',"Dimapur","Kiphire","Kohima","Longleng","Mokokchung","Noklak","Mon","Peren","Phek","Tuensang","Wokha","Zunheboto"];
   $(function() {
  var options = '';
  for (var i = 0; i < nagaland.length; i++) {
      options += '<option value="' + nagaland[i] + '">' + nagaland[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Odisha') {
    var orissa =  ['SELECT DISTRICT',"Angul","Balangir","Balasore","Bargarh","Bhadrak","Boudh",
    "Cuttack","Debagarh","Dhenkanal","Gajapati","Ganjam","Jagatsinghpur","Jaipur","Jharsuguda",
    "Kalahandi","Kandhamal","Kendraparah","Kendujhar","Khorda","Khoraput","Malkangiri","Mayurbhanj","Nabrangpur","Nayagarh",
    "Nuapada","Puri","Rayagada","Sambalpur","Subarnapur","Sundergarh"];
   $(function() {
  var options = '';
  for (var i = 0; i < orissa.length; i++) {
      options += '<option value="' + orissa[i] + '">' + orissa[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Puducherry') {
    var puducherry = ['SELECT DISTRICT',"Karaikal","Mahe","Puducherry","Yanam"];
   $(function() {
  var options = '';
  for (var i = 0; i < puducherry.length; i++) {
      options += '<option value="' + puducherry[i] + '">' + puducherry[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Punjab') {
    var punjab = ['SELECT DISTRICT',"Amritsar","Barnala","Bathinda","Firozpur","Faridkot","Fatehgarh Sahib","Fazilka","Gurdaspur",
    "Hoshiarpur","Jalandhar","Kapurthala","Ludhiana","Mansa","Moga","Mohali","Muktsar","Pathankot",
    "Patiala","Rupnagar","Sangrur","Shaheed Bhagat Singh Nagar","Tarn Taran"];
   $(function() {
  var options = '';
  for (var i = 0; i < punjab.length; i++) {
      options += '<option value="' + punjab[i] + '">' + napunjabgaland[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Rajasthan') {
    var rajasthan = ['SELECT DISTRICT',"Ajmer","Alwar","Baran","Banswara","Barmer","Basni","Bundi","Bharatpur","Bhilwara",
    "Bikaner","Chittorgarh","Churu","Dausa","Dholpur","Dungarpur","Hanumangarh","Jaipur",
    "Jalore","Jhalawar","Jhunjhunu","Jaisalmer","Jodhpur",
    "Karauli","Kota","Nagaur","Pali","Pratapgad","Rajsamand","Sawai Madhopur","Sikar","Sirohi","Sri Ganganagar",
    "Tonk","Udaipur"];
   $(function() {
  var options = '';
  for (var i = 0; i < rajasthan.length; i++) {
      options += '<option value="' + rajasthan[i] + '">' + rajasthan[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Sikkim') {
    var sikkim = ['SELECT DISTRICT',"East Sikkhim","North Sikkhim","South Sikkhim"];
   $(function() {
  var options = '';
  for (var i = 0; i < sikkim.length; i++) {
      options += '<option value="' + sikkim[i] + '">' + sikkim[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Tamil Nadu') {
    var tn = ['SELECT DISTRICT',"Ariyalur"," Chengalpattu","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode","Kanchipuram","Kallakurichi",
    "Kanyakumari","Karur","Krishnagiri","Madurai"," Mayiladuthurai","Nagapattinam","Nilgiris","Namakkal",
    "Perambalur","Pudukkottai","Ramanathapuram","Ranipet","Salem","Sivaganga","Tenkasi","Thanjavur","Thiruvallur","Tiruppur",
    "Tiruchirapalli","Theni","Tirunelveli","Thanjavur","Thoothukudi","Tiruvallur","Tiruvannamalai","Tirupattur",
    "Vellore","Villupuram","Viruthunagar"];
   $(function() {
  var options = '';
  for (var i = 0; i < tn.length; i++) {
      options += '<option value="' + tn[i] + '">' + tn[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Telangana') {
    var telangana = ['SELECT DISTRICT','Adilabad', 'Bhadradri Kothagudem', 'Hyderabad', 'Jagtial', 'Jangaon',
    'Jayashankar', 'Jogulamba', 'Kamareddy', 'Karimnagar', 'Khammam',
    'Komaram Bheem', 'Mahabubabad', 'Mahbubnagar', 'Mancherial', 'Medak',
    'Medchal', 'Mulugu', ' Nagarkurnool', 'Nalgonda', 'Narayanpet', 'Nirmal',
    'Nizamabad', 'Peddapalli', 'Rajanna Sircilla', 'Ranga Reddy',
    'Sangareddy', 'Siddipet', 'Suryapet', 'Vikarabad', 'Wanaparthy',
    'Warangal Rural', 'Warangal Urban', 'Yadadri Bhuvanagiri'];
   $(function() {
  var options = '';
  for (var i = 0; i < telangana.length; i++) {
      options += '<option value="' + telangana[i] + '">' + telangana[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Tripura') {
    var tripura = ['SELECT DISTRICT',' Dhalai', ' Gomati', ' Khowai', ' North Tripura', ' Sepahijala',
    ' South Tripura', ' Unakoti', ' West Tripura'];
   $(function() {
  var options = '';
  for (var i = 0; i < tripura.length; i++) {
      options += '<option value="' + tripura[i] + '">' + tripura[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Uttar Pradesh') {
    var up =  ['SELECT DISTRICT',' Agra', ' Aligarh', ' Ambedkar Nagar', ' Amethi', ' Amroha', ' Auraiya',
    ' Ayodhya', ' Azamgarh', ' Baghpat', ' Bahraich', ' Ballia', 'Balrampur',
    ' Banda', ' Barabanki', ' Bareilly', ' Basti', ' Bhadohi', ' Bijnor', ' Budaun',
    ' Bulandshahr', ' Chandauli', ' Chitrakoot', ' Deoria', ' Etah', ' Etawah',
    ' Farrukhabad', ' Fatehpur', ' Firozabad', ' Gautam Buddha Nagar',
    ' Ghaziabad', ' Ghazipur', ' Gonda', ' Gorakhpur', ' Hamirpur', ' Hapur',
    ' Hardoi', ' Hathras', ' Jalaun', ' Jaunpur', ' Jhansi', ' Kannauj',
    ' Kanpur Dehat', ' Kanpur Nagar', ' Kasganj', ' Kaushambi', ' Kheri',
    ' Kushinagar', ' Lalitpur', ' Lucknow', ' Maharajganj', ' Mahoba', ' Mainpuri',
    ' Mathura', ' Mau', ' Meerut', ' Mirzapur', ' Moradabad', ' Muzaffarnagar',
    ' Pilibhit', ' Pratapgarh', ' Prayagraj', ' Raebareli', ' Rampur',
    ' Saharanpur', ' Sambhal', ' Sant Kabir Nagar', ' Shahjahanpur', ' Shamli',
    ' Shravasti', ' Siddharthnagar', ' Sitapur', ' Sonbhadra', ' Sultanpur',
    ' Unnao', ' Varanasi'];
   $(function() {
  var options = '';
  for (var i = 0; i < up.length; i++) {
      options += '<option value="' + up[i] + '">' + up[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Uttarakhand') {
    var uttarakhand = ['SELECT DISTRICT',' Almora', ' Bageshwar', ' Chamoli', ' Champawat', ' Dehradun', ' Haridwar',
    ' Nainital', ' Pauri', ' Pithoragarh', ' Rudraprayag', ' Tehri',
    ' Udham Singh Nagar', ' Uttarkashi'];
   $(function() {
  var options = '';
  for (var i = 0; i < uttarakhand.length; i++) {
      options += '<option value="' + uttarakhand[i] + '">' + uttarakhand[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='West Bengal') {
    var wb =  ['SELECT DISTRICT',' Alipurduar', ' Bankura', ' Birbhum', ' Cooch Behar', ' Dakshin Dinajpur',
    ' Darjeeling', ' Hooghly', ' Howrah', ' Jalpaiguri', ' Jhargram', ' Kalimpong',
    ' Kolkata', ' Malda', ' Murshidabad', ' Nadia', ' North 24 Parganas',
    ' Paschim Bardhaman', ' Paschim Medinipur', ' Purba Bardhaman',
    ' Purba Medinipur', ' Purulia', ' South 24 Parganas', ' Uttar Dinajpur'];
   $(function() {
  var options = '';
  for (var i = 0; i < wb.length; i++) {
      options += '<option value="' + wb[i] + '">' + wb[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }

  if ($val=='Andaman and Nicobar Islands') {
    var an =  ['SELECT DISTRICT','Nicobar', ' North Middle Andaman', ' South Andaman'];
   $(function() {
  var options = '';
  for (var i = 0; i < an.length; i++) {
      options += '<option value="' + an[i] + '">' + an[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }

  if ($val=='Chandigarh') {
    var chandigarh =  ['SELECT DISTRICT','Chandigarh'];
   $(function() {
  var options = '';
  for (var i = 0; i < chandigarh.length; i++) {
      options += '<option value="' + chandigarh[i] + '">' + chandigarh[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }

  if ($val=='Lakshadweep') {
    var laksh =  ['SELECT DISTRICT','Lakshadweep'];
   $(function() {
  var options = '';
  for (var i = 0; i < laksh.length; i++) {
      options += '<option value="' + laksh[i] + '">' + laksh[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }

  if ($val=='Ladakh') {
    var ladakh =  ['SELECT DISTRICT','Kargil' ,' Leh'];
   $(function() {
  var options = '';
  for (var i = 0; i < ladakh.length; i++) {
      options += '<option value="' + ladakh[i] + '">' + ladakh[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
}

