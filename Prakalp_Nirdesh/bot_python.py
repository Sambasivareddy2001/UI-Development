def hour_wise():
    query = "SELECT State,Region,Hours,count(*) as files FROM schools_detailed where hours between 1 and 8 group by State,Region,hours order by Hours"
    return query
def row_wise():
    query = "SELECT * FROM schools_detailed where hours between 1 and 8"
    return query
def row_wise_paticular(user_input1):
    columns = ['state','district','status']
    #user_input1 = input('Enter Categories like State, District, Region')
    #user_input1 = 'details of files KERALA and TRIVANdru and MADHYA PRADESH'
    user_input2 = user_input1.lower()
    columns_to_filter = {}
    from rapidfuzz import process,fuzz
    def find_closest_matches(user_input2, data_list, threshold=85):
        matches = process.extract(user_input2, data_list, scorer=fuzz.partial_ratio)
        # Filter matches by threshold
        return [match[0] for match in matches if match[1] >= threshold]
    columns_to_filter = {}
    matches = find_closest_matches(user_input2, columns)
    #print(matches)
    #where_clauses = []
#group_by_columns = []
    if len(matches)>0:
            #group_by_columns.append(column)
        query = f"SELECT {', '.join(matches)},count(*) as Files FROM schools_detailed GROUP BY {', '.join(matches)}"
        return query
def hour_wise_paticular(user_input1):
    columns = ['state','district','status']
    #user_input1 = input('Enter Categories like State, District, Region')
    #user_input1 = 'details of files KERALA and TRIVANdru and MADHYA PRADESH'
    user_input2 = user_input1.lower()
    columns_to_filter = {}
    from rapidfuzz import process,fuzz
    def find_closest_matches(user_input2, data_list, threshold=85):
        matches = process.extract(user_input2, data_list, scorer=fuzz.partial_ratio)
        # Filter matches by threshold
        return [match[0] for match in matches if match[1] >= threshold]
    columns_to_filter = {}
    matches = find_closest_matches(user_input2, columns)
    #print(matches)
    #where_clauses = []
#group_by_columns = []
    if len(matches)>0:
        matches.append('Hours')
            #group_by_columns.append(column)
        query = f"SELECT {', '.join(matches)},count(*) as Files FROM schools_detailed GROUP BY {', '.join(matches)}"
        return query
search_columns = {
        "state": ['MAHARASHTRA', 'KERALA', 'PUNJAB', 'DELHI', 'ARUNACHAL PRADESH',
       'UTTAR PRADESH', 'BIHAR', 'MADHYA PRADESH', 'JHARKHAND', 'HARYANA',
       'RAJASTHAN', 'KARNATAKA', 'CHATTISGARH', 'FOREIGN SCHOOLS',
       'ODISHA', 'WEST BENGAL', 'TELANGANA', 'TAMILNADU',
       'JAMMU & KASHMIR', 'ANDHRA PRADESH', 'ANDAMAN & NICOBAR',
       'GUJARAT', 'UTTARAKHAND', 'SIKKIM', 'ASSAM', 'CHANDIGARH',
       'HIMACHAL PRADESH', 'TRIPURA', 'GOA', 'MIZORAM', 'MANIPUR',
       'PUDUCHERRY', 'MEGHALAYA', 'LAKSHADWEEP', 'NAGALAND',
       'DADAR & NAGAR HAVELI', 'DAMAN & DIU'],
        "district": ['JALGAON', 'KOZHIKODE', 'JULLUNDUR', 'PAPUMPARA', 'AGRA',
       'PATNA', 'BHOPAL', 'BOKARO', 'SONEPAT', 'LATUR', 'ROPAR', 'KOLLAM',
       'BANGALORE', 'GAUTAM BUDH NAGAR', 'DURG', 'RAISEN', 'BAHRAIN',
       'BIKANER', 'MYSORE', 'DEORIA', 'KAITHAL', 'HYDERABAD',
       'TIRUVANNAMALAI', 'JHUNJHUNU', 'BIJNOUR', 'JAMMU', 'VISAKHAPATNAM',
       'MALAPPURAM', 'NEPAL', 'VADODARA (BARODA)', 'RUDRAPRAYAG',
       'COIMBATORE', 'KOTA', 'DHUBRI', 'SONEBHADRA', 'SURAT', 'HARIDWAR',
       'EAST DISTRICT', 'PERIYAR', 'KANPUR', 'EAST SINGHBHUM', 'GWALIOR',
       'MOGA', 'CHANDRAPUR', 'NORTH WEST DELHI', 'HOSHANGABAD',
       'SHOLAPUR', 'JAIPUR', 'VARANASI', 'NORTH EAST DELHI', 'KOTTAYAM',
       'MANGALORE', 'NALGONDA', 'KARNAL', 'FARRUKHABAD', 'KORIYA',
       'INDORE', 'WEST DELHI', 'UNNAO', 'NELLORE', 'VIDISHA',
       'THIRUVANANTHAPURAM', 'UDHAM SINGH NAGAR', 'MIRZAPUR',
       'NAWANSHAHR', 'KANNUR', 'JHARSUGUDA', 'GOPALGANJ', 'BHAGALPUR',
       'RAMPUR', 'MOHALI', 'WARDHA', 'KOKRAJHAR', 'UNITED ARAB EMIRATES',
       'MAHINDERGARH', 'JHANSI', 'REWA', 'MANSA', 'MATHURA', 'AMBALA',
       'KHARGAON', 'MADHUBANI', 'BALIA', 'KANYAKUMARI', 'MANDI',
       'YAMUNANAGAR', 'SARAN (CHAPRA)', 'GHAZIABAD', 'WEST GODAVARI',
       'ALLAHABAD', 'SAUDI ARABIA', 'AMRITSAR', 'KHURDA', 'MORADABAD',
       'DIBRUGARH', 'BAGHPAT', 'DEHRADUN', 'WEST DISTRICT', 'LEH',
       'RANGAREDDY', 'ALIGARH', 'KANCHEEPURAM', 'DHARWAD', 'SONITPUR',
       'MEERUT', 'GONDIYA', 'PUNE', 'BIJAPUR', 'CHANDAULI', 'GIRIDIH',
       'RANCHI', 'FARIDKOT', 'THRISSUR', 'NAGPUR', 'HATHRAS', 'BELGAUM',
       'TARANTARAN', 'LUCKNOW', 'MUZAFFARPUR', 'SEHORE', 'SOUTH TRIPURA',
       'WAYANAD', 'EAST DELHI', 'DHANBAD', 'UDHAMPUR', 'NAINITAL',
       'REWARI', 'CHITTORGARH', 'KOLAR', 'CALCUTTA', 'IDUKKI',
       'SRI GANGANAGAR', 'DHAR', 'BHATINDA', 'FEROZEPUR', 'KAMRUP',
       'AKBARPUR', 'PURNEA', 'HOSHIARPUR', 'SANT RAVIDAS NAGAR',
       'HAMIRPUR', 'LUDHIANA', 'RAYAGADA', 'BELLARY', 'MORENA', 'NAGAON',
       'PALWAL', 'BALOD', 'KURNOOL', 'LAKHIMPUR KHERI', 'ERNAKULAM',
       'KURUKESHTRA', 'PATHANKOT', 'OSMANABAD', 'GULBARGA', 'BOLANGIR',
       'GONDA', 'KUWAIT', 'GORAKHPUR', 'NORTH DELHI', 'CHITRADURGA',
       'AHMEDABAD', 'AURANGABAD', 'GURDASPUR', 'MUZAFFARNAGAR',
       'PALAKKAD', 'RAI BARELI', 'UDAIPUR', 'FATEHABAD', 'JABALPUR',
       'SANGRUR', 'PATHANAMTHITTA', 'JIND', 'BULANDSHAHAR',
       'SOUTH WEST DELHI', 'NORTH KANNADA', 'RAIGAD', 'HISSAR', 'BASTAR',
       'KABRI ANGLONG', 'TUMKUR', 'GANJAM', 'HANUMANGARH', 'SALEM',
       'CHAMOLI', 'ETAH', 'CHITTOOR', 'NORTH DISTRICT', 'BAGESHWAR',
       'GANDHINAGAR', 'SOLAN', 'PORT BLAIR', 'ETAWAH', 'JALPAIGURI',
       'MEHSANA', 'SHIVPURI', 'DEOGARH', 'IDDUKI', 'BHILWARA', 'BADWANI',
       'RATLAM', 'CUDDAPAH', 'KANNOJ', 'DANTEWADA', 'BAREILLY', 'UDUPI',
       'SULTANPUR', 'MAYURBHANJ', 'PATIALA', 'FARIDABAD', 'JAUNPUR',
       'SANGLI', 'SAHARANPUR', 'ROHTAK', 'CHAMBA', 'GOLAGHAT',
       'NARSIMHAPUR', 'VAISHALI (HAJIPUR)', 'CHANGLANG', 'WEST TRIPURA',
       'PULWAMA', 'CHHINDWARA', 'GHAZIPUR', 'CHAMPARAN EAST', 'SIRMOUR',
       'CHENNAI', 'GUNTUR', 'GOA (NORTH)', 'SURGUJA', 'DEWAS',
       'SUNDARGARH', 'KASARGUD', 'PITHORAGARH', 'BARAMULLA', 'ALWAR',
       'HAVERI', 'DUNGARPUR', 'RAJNANDGAON', 'KATNI',
       'CH. SHAHUJI MAHARAJ NAGAR', 'CHHATARPUR', 'PALAMAU', 'EAST SIANG',
       'KOLHAPUR', 'DARBHANGA', 'AZAMGARH', 'HAZARIBAGH', 'BALRAMPUR',
       'PANCHKULA', 'VALSAD', 'HAILAKANDI', 'BAGALKOT', 'BHIWANI',
       'MAHARAJGANJ', 'KALAHANDI', 'FATEHGARH', 'GURGAON', 'GUNA',
       'PRAKASAM', 'SIRSA', 'SAGAR', 'CUTTACK', 'SAHAJANPUR', 'AIZAWAL',
       'CHICKMAGALUR', 'THANE', 'MIDNAPUR', 'JHALAWAR', 'SOUTH DELHI',
       'BUNDI', 'SAMASTIPUR', 'MUKTSAR', 'CHAMPARAN WEST', 'KAPURTHALA',
       'DAVANGERE', 'MUMBAI', 'MAINPURI', 'ANANTNAG', 'KUTCH-BHUJ',
       'SRIKAKULAM', 'FATEHPUR', 'KUSHI NAGAR', 'RAIPUR', 'SHIMOGA',
       'DINDIGUL', 'ROHTAS', 'BEGUSARAI', 'NORTH 24-PARGANA', 'CACHAR',
       'TEHRI-GARHWAL', 'SABARKANTHA/HIMMATNAGAR', 'JODHPUR', 'ALAPPUZHA',
       'SHAHDOL', 'SARAIKELA KHARSN', 'PANIPAT', 'NANDURBAR', 'SIROHI',
       'JAMTARA', 'COOCH BEHAR', 'ANGUL', 'NASIK', 'SHAJAPUR',
       'CHANDIGARH(UT)', 'BILASPUR', 'SECUNDERABAD', 'BANSWARA',
       'JHAJJAR', 'KULU', 'BIDAR', 'IMPHAL', 'ITANAGAR', 'PALI',
       'KATIHAR', 'THANJAVUR', 'KORAPUT', 'KANGRA', 'AJMER', 'MAHOBA',
       'NORTH ARCOT AMBEDKAR', 'PERAMBALUR', 'QATAR', 'JAMNAGAR',
       'KHAMMAM', 'SOUTH DISTRICT', 'WARANGAL', 'AMRAVATI', 'SAHARSA',
       'EAST GODAVARI', 'KODERMA', 'RAJKOT', 'SEONI', 'KARAIKAL',
       'TIRUNELVELI', 'BURHANPUR', 'THOUBAL', 'BARGARH', 'FEROZABAD',
       'KRISHNA', 'JYOTIBA PHULE NAGAR', 'SAMBALPUR', 'NALANDA', 'SATARA',
       'ERODE', 'BHOJPUR', 'BARMER', 'PURULIA', 'N.C.HILLS', 'DAUSA',
       'SIDHI', 'KHANDWA', 'CHENNAI CITY', 'NEW MUMBAI', 'PORBANDAR',
       'GAYA', 'SHEOPUR', 'TONK', 'HOOGHLY', 'EAST KHASI HILLS',
       'DHAMTARI', 'UPPER SUBANSIRI', 'SILIGURI', 'JAJPUR', 'PILIBHIT',
       'LIBERIA', 'KODAGU', 'BASTI', 'BALAGHAT', 'CENTRAL DELHI',
       'HARDOI', 'VIRUDH NAGAR', 'HARDA', 'ARARIA', 'RAJASMAND',
       'GOALPARA', 'BHUJ', 'BURDWAN', 'PAURI GARHWAL', 'SOUTH 24-PARGANA',
       'JHABUA', 'AMRELI', 'UJJAIN', 'TIRUCHIRAPALI', 'BETUL',
       'ANANATPUR', 'MADHEPURA', 'YAVAT MAL', 'NUAPADA', 'MURSHIDABAD',
       'VELLORE', 'KURUNG KUMEY', 'NAGAUR', 'DAMOH', 'TUENSANG', 'GADAG',
       'BIRBHUM', 'BADAUN', 'BHARATPUR', 'NAWADAH', 'SIKAR', 'KANDHAMAL',
       'BEED', 'WEST SIANG', 'MAHE', 'THIRUVALLUR', 'SIMLA',
       'MAHBUBNAGAR', 'MAU', 'AHMEDNAGAR', 'RAMANATHAPURAM', 'KHEDA',
       'KAIMUR', 'SIMDEGA', 'PANNA', 'BHARUCH', 'TINSUKHIA', 'CHURU',
       'DHARMAPURI', 'NADIA', 'ANDAMAN', 'MANDYA', 'JAISALMER',
       'KHAGARIA', 'SITAMARHI', 'DATIA', 'BUXAR', 'BANASKANTHA/PALANPUR',
       'LAHAUL & SPITI', 'KHORDHA', 'UMARIA', 'BARAN', 'MEDAK', 'MEWAT',
       'RAICHUR', 'BULDHANA', 'KEONJHAR', 'ANAND', 'VILLUPURAM',
       'SANT KABIR NAGAR', 'EAST TRIPURA', 'NORTH DINAJPUR', 'FAIZABAD',
       'LAKSHADWEEP', 'JANGIR-CHAMPA', 'BANKA', 'NAMAKKAL', 'BARABANKI',
       'KARAULI', 'SHEIKHPURA', 'BONGAIGAON', 'PEREN', 'JATSINGHPUR',
       'OMAN', 'KOPPAL', 'PURI', 'BAKSA', 'PONDICHERRY', 'JALAUN',
       'BHADRAK', 'SAHIBGANJ', 'MALAYSIA', 'JASHPUR', 'MADURAI',
       'DADAR & NAGAR HAVELI', 'LAKHIMPUR', 'CHENGALPATTU', 'ALMORA',
       'HAPUR', 'SINGAPORE', 'NAVSARI', 'KHANNA', 'MUNGER', 'KAUSHAMBI',
       'RAJGARH', 'TIKAMGARH', 'DHULE', 'WEST SINGHBHUM', 'CHATRA',
       'PARTAPGARH', 'KAWARDHA', 'KARIMNAGAR', 'SINDHDURG',
       'JAINTIA HILLS', 'THOOTHUKUDI', 'SATNA', 'GARHWA', 'SHRAVASTI',
       'DIBANG VALLEY', 'BHADOHI', 'SOUTH KANNADA', 'CHURACHANDPUR',
       'KATHUA', 'JUNAGARH', 'MALDA', 'PASUMPON-MUTHURAMALINGA T',
       'KENDRAPARA', 'NEEMUCH', 'KUPWARA', 'NALBARI', 'JALNA', 'KARUR',
       'MANDSAUR', 'NEW DELHI', 'SOUTH DINAJPUR', 'NIZAMABAD', 'SIBSAGAR',
       'WEST KEMENG', 'AKOLA', 'TIRUNELVELI KATTABOMMAN', 'CUDDALORE',
       'BHANDARA', 'DARRANG', 'SITAPUR', 'UPPER SIANG', 'CHITRAKOOT',
       'KARIMGANJ', 'HASSAN', 'UNA', 'WEST GARO HILLS', 'KORBA',
       'SINGHROULI', 'BARNALA', 'UKHRUL', 'TAWANG', 'NORTH TRIPURA',
       'BHAVNAGAR', 'BAHRAICH', 'KANKER', 'UTTARKASHI', 'CHAMPAWAT',
       'DARJEELING', 'GUMLA', 'NANDED', 'V.O.C.', 'SBS NAGAR', 'DINDORI',
       'JAHANABAD', 'DIMAPUR', 'PARBHANI', 'RAIGARH', 'KISHANGANJ',
       'BANDA', 'SRINAGAR', 'DHOLPUR', 'SIWAN', 'ANJAW', 'PHEK',
       'SWAI MADHOPUR', 'GADCHIROLI', 'PUDUKOTTAI', 'LALITPUR', 'AURAIYA',
       'DANG-AHWA', 'REPUBLIC OF BENIN', 'MAHASUMUND', 'NARNAUL',
       'SONEPUR', 'HINGOLI', 'SURENDRANAGAR', 'MANDLA', 'VIZIANAGARAM',
       'SENAPATI', 'HOWRAH', 'LATEHAR', 'GODDA', 'DHENKANAL', 'LOHIT',
       'CITY GUWAHATI', 'SHAMLI', 'KRISHNAGIRI', 'ADILABAD', 'BANKURA',
       'PAKUR', 'SUPAUL', 'ROORKEE', 'JORHAT', 'BALASORE', 'GOA (SOUTH)',
       'LIBYA', 'SAMBHAL', 'KISHTWAR', 'JAMUI', 'ZUNHEBOTO', 'DURGAPUR',
       'MORIGAON', 'KANSHI RAM NAGAR', 'WASHIM', 'ETHIOPIA',
       'THE NILGIRIS', 'TIRAP', 'BHIND', 'RAJOURI', 'SURAJPUR',
       'CHAMARAJA NAGAR', 'CHANDEL', 'JALLORE',
       'VAIGAI VEERAN ALAGAMUTHU', 'DAMAN', 'EAST KEMENG', 'THAILAND',
       'YEMEN', 'PUDUKKOTTAI', 'FAZILKA', 'KOHIMA', 'TANSANIA',
       'LOWER SUBANSIRI', 'GAJAPATI', 'TAMENGLONG', 'DODA', 'SHERCHHIP',
       'RATNAGIRI', 'HALDWANI', 'LAKHISARAI', 'PATAN', 'NAGAPATTINAM',
       'NORTH ARCOT', 'PANCHMAHAL (GODHRA)', 'KARGIL', 'WOKHA',
       'NAYAGARH', 'LUNGELI', 'BARPETA', 'SOUTH ARCOT', 'UGANDA',
       'POONCH', 'SIDDHARTH NAGAR', 'VIJAYAWADA', 'MALKANGIRI',
       'EAST GARO HILLS', 'MYANMAR', 'MOKOKCHUNG', 'DUMKA',
       'P.T.T DISTRICT', 'RAMGARH', 'BANGLADESH', 'KINNAUR', 'DIU',
       'BISHNUPUR', 'RI-BHOI', 'IRAN', 'DHEMAJI', 'DOHAD', 'MANIPUR EAST',
       'NOWRANGPUR', 'JAPAN', 'BADGAM', 'BERHAMPUR', 'MANIPUR CENTRAL',
       'SAMBA', 'NIGERIA', 'SURAT GARH', 'SHEOHAR', 'NARMADA', 'MON',
       'INDONESIA', 'DEVBHUMI DWARKA', 'BOUDH', 'PADRAUNA',
       'MANIPUR WEST', 'QUIDE MILLATH', 'ASANSOL', 'RUSSIA', 'LOHERDAGA',
       'KIPHIRE', 'PHULBANI', 'KOLASIB', 'WEST KHASI HILLS', 'GHANA'],
        'region':['CHENNAI', 'TRIVANDRUM', 'PANCHKULA', 'DELHI', 'GUWAHATI',
       'ALLAHABAD', 'PATNA', 'AJMER', 'DEHRADUN', 'BHUBANESWAR'],
        "status":['Middle Class', 'Senior Secondary', 'Secondary School'],
    }
def row_wise_paticular_value(purpose,user_input1):    
    for key in search_columns:
        search_columns[key] = [item.lower() for item in search_columns[key]]
    #user_input1 = input('Enter Category Value like Kadapa, Andhra')
    #user_input1 = 'details of files KERALA and TRIVANdru and MADHYA PRADESH'
    user_input2 = user_input1.lower()
    user_input2
    
    columns_to_filter = {}
    from rapidfuzz import process,fuzz
    def find_closest_matches(user_input2, data_list, threshold=85):
        matches = process.extract(user_input2, data_list, scorer=fuzz.partial_ratio)
        # Filter matches by threshold
        return [match[0] for match in matches if match[1] >= threshold]
    columns_to_filter = {}
    for column,values in search_columns.items():
        matches = find_closest_matches(user_input2, values)
        #print(matches)
        if matches:
            columns_to_filter[column] = matches
    where_clauses = []
    group_by_columns = []
    for column, values in columns_to_filter.items():
        conditions = " OR ".join([f"{column} LIKE '%{value}%'" for value in values])
        where_clauses.append(f"({conditions})")
        if purpose ==3:
            query = f"SELECT * FROM schools_detailed WHERE {' AND '.join(where_clauses)};"
    return query
def row_wise_paticular_value1(purpose,user_input1):    
    for key in search_columns:
        search_columns[key] = [item.lower() for item in search_columns[key]]
    #user_input1 = input('Enter Category Value like Kadapa, Andhra')
    #user_input1 = 'details of files KERALA and TRIVANdru and MADHYA PRADESH'
    user_input2 = user_input1.lower()
    user_input2
    
    columns_to_filter = {}
    from rapidfuzz import process,fuzz
    def find_closest_matches(user_input2, data_list, threshold=85):
        matches = process.extract(user_input2, data_list, scorer=fuzz.partial_ratio)
        # Filter matches by threshold
        return [match[0] for match in matches if match[1] >= threshold]
    columns_to_filter = {}
    for column,values in search_columns.items():
        matches = find_closest_matches(user_input2, values)
        #print(matches)
        if matches:
            columns_to_filter[column] = matches
    where_clauses = []
    group_by_columns = []
    for column, values in columns_to_filter.items():
        conditions = " OR ".join([f"{column} LIKE '%{value}%'" for value in values])
        where_clauses.append(f"({conditions})")
        group_by_columns.append(column)
        if purpose ==3:
            query = f"SELECT {', '.join(group_by_columns)},count(*) as Files FROM schools_detailed Where {' AND '.join(where_clauses)} GROUP BY {', '.join(group_by_columns)}"
    return query
def hour_wise_paticular_value1(purpose,user_input1):    
    for key in search_columns:
        search_columns[key] = [item.lower() for item in search_columns[key]]
    #user_input1 = input('Enter Category Value like Kadapa, Andhra')
    #user_input1 = 'details of files KERALA and TRIVANdru and MADHYA PRADESH'
    user_input2 = user_input1.lower()
    user_input2
    
    columns_to_filter = {}
    from rapidfuzz import process,fuzz
    def find_closest_matches(user_input2, data_list, threshold=85):
        matches = process.extract(user_input2, data_list, scorer=fuzz.partial_ratio)
        # Filter matches by threshold
        return [match[0] for match in matches if match[1] >= threshold]
    columns_to_filter = {}
    for column,values in search_columns.items():
        matches = find_closest_matches(user_input2, values)
        #print(matches)
        if matches:
            columns_to_filter[column] = matches
    where_clauses = []
    group_by_columns = []
    for column, values in columns_to_filter.items():
        conditions = " OR ".join([f"{column} LIKE '%{value}%'" for value in values])
        where_clauses.append(f"({conditions})")
        group_by_columns.append(column)
        group_by_columns.append('Hours')
    if purpose ==3:
        query = f"SELECT {', '.join(group_by_columns)},count(*) as Files FROM schools_detailed Where {' AND '.join(where_clauses)} GROUP BY {', '.join(group_by_columns)}"
    return query
columns = ['state','district','status']
user_input1 = input('Enter number of files in state')
#user_input1 = 'details of files KERALA and TRIVANdru and MADHYA PRADESH'
user_input2 = user_input1.lower()

    
columns_to_filter = {}
from rapidfuzz import process,fuzz
def find_closest_matches1(user_input2, data_list, threshold=85):
    matches1 = process.extract(user_input2, data_list, scorer=fuzz.partial_ratio)
        # Filter matches by threshold
    return [match[0] for match in matches1 if match[1] >= threshold]
columns_to_filter = {}
matches1 = find_closest_matches1(user_input2, columns)

for key in search_columns:
    search_columns[key] = [item.lower() for item in search_columns[key]]  
def find_closest_matches3(user_input2, data_list, threshold=85):
    global matches3
    matches3 = process.extract(user_input2, data_list, scorer=fuzz.partial_ratio)
        # Filter matches by threshold
    return [match[0] for match in matches3 if match[1] >= threshold]
list1 = []
for column,values in search_columns.items():
    matches3 = find_closest_matches3(user_input2, values)
    #print(matches3)
    if len(matches3)>0:
        list1.append(1)
if len(list1)>0:
    purpose = 3
    if 'hour' in user_input2:
        option = 1
    elif 'hour' not in user_input2 and 'number' in user_input2:
        option = 2
    elif 'details' in user_input2:
        option = 3
elif len(matches1)>0:
    purpose = 2
    if 'hour' in user_input2:
        option = 1
    elif 'hour' not in user_input2:
        option = 2
else:
    purpose = 1
    if 'hour' in user_input2:
        option = 1
    elif 'hour' not in user_input2:
        option = 2
result = None
def Main_function2(purpose,option,user_input1):
    #print(purpose,option)
    if purpose ==1:
        global result
        if option ==1:
            result = hour_wise()
        elif option == 2:
            result = row_wise()
    elif purpose ==2:
        if option ==1:
            result = hour_wise_paticular(user_input1)
        elif option == 2:
            result = row_wise_paticular(user_input1)
    elif purpose ==3:
        if option ==1:
            result = hour_wise_paticular_value1(purpose,user_input1)
        elif option ==2:
            result = row_wise_paticular_value(purpose,user_input1)
        elif option == 3:
            result = row_wise_paticular_value1(purpose,user_input1)
    return result
import mysql.connector
password1 = input("please enter your password for Mysql")
krishnadb = mysql.connector.connect(host = "localhost",user = "root",password = password1 ,database = "sakila")
cursor = krishnadb.cursor()
#cursor.execute('create database Krishna;')
cursor.execute('use Krishna;')
query_result = None
def Main2(purpose,option,user_input1):
    #print(purpose,option,user_input1)
    global query_result
    query_result = Main_function2(purpose,option,user_input1)
    #print(query_result)
    data = pd.read_sql_query(query_result,krishnadb)
    return data
from flask import Flask, request, render_template_string
import pandas as pd
# intialise data of lists.
df = Main2(purpose,option,user_input1)
print(df)
app = Flask(__name__)

# HTML template with a text box
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Input Form</title>
</head>
<body>
    <h1>Welcome to the Flask App!</h1>
    <p>
        Instructions:
        <ol>
            <li>If you need hour-wise pivoted details, type the keyword "hour".</li>
            <li>To get the number of files for categories without the hour, type a specific category with the keyword "number".</li>
            <li>For file-level details for categories, type the keyword "detail".</li>
            <li>If you need file-level details of all states and districts, type "details of state and districts".</li>
            <li>For hour-wise details of states and districts, type "hour-wise files and district".</li>
        </ol>
    </p>
    <form method="post" action="/">
        <label for="user_input">Enter your input:</label>
        <input type="text" id="user_input" name="user_input" required>
        <button type="submit">Submit</button>
    </form>
    {% if output %}
    <h3>Result:</h3>
    {{ output | safe }}
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    output = None
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        # Add custom processing logic for the input here
        if user_input.lower() == 'hour':
            output = df.to_html(classes='table table-bordered')
        elif user_input.lower() == 'number':
            output = df.to_html(classes='table table-bordered')
        elif user_input.lower() == 'detail':
            output = df.to_html(classes='table table-bordered')
        elif user_input.lower() == 'details of state and districts':
            output = df.to_html(classes='table table-bordered')
        elif user_input.lower() == 'hour-wise files and district':
            output = df.to_html(classes='table table-bordered')
        else:
            output = f"Invalid input: {user_input}"
    return render_template_string(html_template, output=output)

if __name__ == '__main__':
    app.run(debug=True)
