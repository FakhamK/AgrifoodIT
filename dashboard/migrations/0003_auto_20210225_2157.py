# Generated by Django 3.1.6 on 2021-02-25 20:57

from django.db import migrations


# https://docs.djangoproject.com/en/3.1/topics/migrations/#data-migrations
def seed_pig_table(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Pig = apps.get_model('dashboard', 'Pig')
    pig_data = {
        "1A": "E280689000000002333A4CA2",
        "1B": "E200001999130116107056CE",
        "2A": "E280689000000002333A634E",
        "2B": "E200001999130113085050B4",
        "3A": "E2806890000000023338DD61",
        "3B": "E20000195206006314302257",
        "4A": "E2806890000000023338D7D3",
        "4B": "E200001952060148155078EA",
        "5A": "E280689000000002333A4CAA",
        "5B": "E2000019520602651540EA7C",
        "6A": "E280689000000002333856BA",
        "6B": "E20000195206018413509C34",
        "7A": "E28068900000000233385B2A",
        "7B": "E2000019991100851580391E",
        "8A": "E2806890000000023337DFFF",
        "8B": "E2000019520602221340C59F",
        "9A": "E28068900000000233383F23",
        "9B": "E20000199913008426803356",
        "10A": "E2806890000000023338DF7C",
        "10B": "E20000195206009213503D52",
        "11A": "E20000199911008725303A93",
        "11B": "E2000019520600431420150D",
        "12A": "E20000195206009913504915",
        "12B": "E200001952060156151081BA",
        "13A": "E200001952060155142085E5",
        "13B": "E2000019520602751510F3D5",
        "14A": "E2000019991300432420169D",
        "14B": "E2000019520602501510E1D1",
        "15A": "E20000195206014414507050",
        "15B": "E20000199913008027502B94",
        "16A": "E2000019520600191460056D",
        "16B": "E2000019991301131700520C",
        "17A": "E20000195206003415500C99",
        "17B": "E200001999130115055058D1",
        "18A": "E20000199913005325401D36",
        "18B": "E2000019520602661540ED25",
        "19A": "E200001999130097264042CC",
        "19B": "E200001952060087146038EF",
        "20A": "E20000195206011214904DA0",
        "20B": "E20000199913011302004FC0",
        "21A": "E20000199911008515903926",
        "21B": "E2000019520602481340DB88",
        "22A": "E2000019520602541340E20F",
        "22B": "E200001999110084044036D6",
        "23A": "E2000019991301090440501E",
        "23B": "E2000019991100861350356F",
        "24A": "E20020199913009827704349",
        "24B": "E200001999110087150038FF",
        "25A": "E20000199913007124202B1F",
        "25B": "E2000019520602021460B565",
        "26A": "E2000019520602571390E4A4",
        "26B": "E2000019520601851510A024",
        "27A": "E20000195206013315106BC6",
        "27B": "E20000199913008024302C14",
        "28A": "E2000019520602551460E4BB",
        "28B": "E20000199913008525203A8A",
        "29A": "E20000199913010125604AEA",
        "29B": "E20000195206010614704DA9",
        "30A": "E20000195206002415700394",
        "30B": "E2000019520602501570E1B5",
        "31A": "E20000199913006725702B51",
        "31B": "E20000195206017714909774",
        "32A": "E20000195206013115306BC1",
        "32B": "E2000019520602821480F5AD",
        "33A": "E20000199913011622205502",
        "33B": "E20000199913009226603B4A",
        "34A": "E2000019520602881480F5B0",
        "34B": "E2000019520602851470F702",
        "35A": "E20000199913011219804CD8",
        "35B": "E2000019520602521370E206",
        "36A": "E20000195206006815802602",
        "36B": "E2000019520601951460B10D",
        "37A": "E2000019520602001390AD34",
        "37B": "E20000195206018414109C18",
        "38A": "E2000019520602511410E4B5",
        "38B": "E2000019520602131430C146",
        "39A": "E20000199913008525103A96",
        "39B": "E20000195206006215701EF7",
        "40A": "E200001952060018141003D1",
        "40B": "E20000199913010127904B56",
        "41A": "E200001952060134137067AF",
        "41B": "E20000195206007314202990",
        "42A": "E200001952060123148062FD",
        "42B": "E20000195206015315707D5C",
        "43A": "E20000199913007624302C12",
        "43B": "E20000195206010014804546",
        "44A": "E20000195206010814404DB2",
        "44B": "E200001952060027140009C9",
        "45A": "E2000019520602621460E7EF",
        "45B": "E20000195206007214802628",
        "46A": "E2000019520601011560495A",
        "46B": "E2000019520602261560CCF1",
        "47A": "E20000195206010315104957",
        "47B": "E2000019520601501450790F",
        "48A": "E20000195206009215703CF6",
        "48B": "E2000019991301002770434A",
        "49A": "E2000019520602821410F5D1",
        "49B": "E2000019520602191530C935",
        "50A": "E2000019520602521530E1C6",
        "50B": "E20000195206003915100F3B"
    }
    for pig in pig_data:
        new_row = Pig(rfid=pig_data[pig], nickname=pig)
        new_row.save()


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0002_auto_20210225_2152'),
    ]

    operations = [
        # https://docs.djangoproject.com/en/3.1/topics/migrations/#data-migrations
        migrations.RunPython(seed_pig_table),
    ]
