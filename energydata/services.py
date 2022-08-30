
SECONDS_IN_AN_HOUR = 3600
WATTS_TO_KILOWATTS = 1000

def computeKwh(queryset):
    total_kwh = 0 
    for x in range(len(queryset)-1):
        # area = h (a+b)/2
        nth = queryset[x]
        nth_1 = queryset[x+1]

        height = (nth_1.timestamp - nth.timestamp ).total_seconds()

        total_kwh = height * (nth.inst_power + nth_1.inst_power)/(2 * SECONDS_IN_AN_HOUR * WATTS_TO_KILOWATTS) + total_kwh
        #end of computation    

    return "{:.4f}".format(total_kwh)  


def computeKwhProfile(queryset):
    profile = []

    for x in range(len(queryset)-1):
        # area = h (a+b)/2
        nth = queryset[x]
        nth_1 = queryset[x+1]

        height = (nth_1.timestamp - nth.timestamp ).total_seconds()

        total_kwh = height * (nth.inst_power + nth_1.inst_power)/(2 * SECONDS_IN_AN_HOUR * WATTS_TO_KILOWATTS)

        data = {}
        data["start_date"] = nth.timestamp
        data["end_date"] = nth_1.timestamp
        data["kwh"] = "{:.4f}".format(total_kwh)

        profile.append(data)
        #end of computation    


    return profile