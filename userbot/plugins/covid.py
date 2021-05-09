# corona virus stats for GoodCatX
from covid import Covid

from . import covidindia


@bot.on(admin_cmd(pattern="covid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="covid(?: |$)(.*)", allow_sudo=True))
async def corona(event):
    if event.pattern_match.group(1):
        country = (event.pattern_match.group(1)).title()
    else:
        country = "World"
    catevent = await edit_or_reply(event, "__Collecting data...__")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data["confirmed"] + country_data["new_cases"]
        hmm2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\n⚠️ Confirmed   : <i>{hmm1}</i>"
        data += f"\n😔 Active           : <i>{country_data['active']}</i>"
        data += f"\n⚰️ Deaths         : <i>{hmm2}</i>"
        data += f"\n🤕 Critical          : <i>{country_data['critical']}</i>"
        data += f"\n😊 Recovered   : <i>{country_data['recovered']}</i>"
        data += f"\n💉 Total tests    : <i>{country_data['total_tests']}</i>"
        data += f"\n🥺 New Cases   : <i>{country_data['new_cases']}</i>"
        data += f"\n😟 New Deaths : <i>{country_data['new_deaths']}</i>"
        await catevent.edit(
            "<b>Corona Virus Info of {}:\n{}</b>".format(country, data),
            parse_mode="html",
        )
    else:
        data = await covidindia(country)
        if data:
            cat1 = int(data["new_positive"]) - int(data["positive"])
            cat2 = int(data["new_death"]) - int(data["death"])
            cat3 = int(data["new_cured"]) - int(data["cured"])
            result = f"<b>Corona virus info of {data['state_name']}\
                \n\n⚠️ Confirmed   : <i>{data['new_positive']}</i>\
                \n😔 Active           : <i>{data['new_active']}</i>\
                \n⚰️ Deaths         : <i>{data['new_death']}</i>\
                \n😊 Recovered   : <i>{data['new_cured']}</i>\
                \n🥺 New Cases   : <i>{cat1}</i>\
                \n😟 New Deaths : <i>{cat2}</i>\
                \n😃 New cured  : <i>{cat3}</i> </b>"
            await catevent.edit(result, parse_mode="html")
        else:
            await edit_delete(
                catevent,
                "__Corona Virus Info of {} is not avaiable or unable to fetch__".format(
                    country
                ),
                5,
            )


CMD_HELP.update(
    {
        "covid": "**Plugin : **__covid__\
        \n\n  •  **Syntax : **__.covid <country name>__\
        \n  •  **Function :** __Get an information about covid-19 data in the given country.__\
        \n\n  •  **Syntax : **__.covid <state name>__\
        \n  •  **Function :** __Get an information about covid-19 data in the given state of India only.__\
        "
    }
)
