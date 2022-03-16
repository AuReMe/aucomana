from reactions_loss import Reactions
from pandas_ods_reader import read_ods


def reactions_from_file(file):
    reactions = []
    d = read_ods(file)
    for i in range(d.shape[0]):
        r = d.loc[i, "Identifiant Metacyc"]
        reactions.append(r)
    return reactions


JSON = "json"
TXT = "txt"

# ###Description ###

# 40 : run 40+7
# 01 : run Pauline all species
# A0 : run Alexandre
# A1 : run Pauline, Alexandre like exactly
# A2 : run Pauline, Alexandre like improved

# ### FILES ####

DATA_FILE_01 = "data/run01_reactions.tsv"
DATA_FILE_40 = 'data/run40_reactions.tsv'
DATA_FILE_A0 = 'data/runA0_reactions.tsv'
DATA_FILE_A1 = 'data/runA1_reactions.tsv'
DATA_FILE_A2 = 'data/runA2_reactions.tsv'
DATA_LELSB_LOSSES = "data/Lelsb_losses.ods"

# ### Select species ###

BROWN_ALGAE_40 = ['Thalassiosira_pseudonana',
                  'Fragilariopsis_cylindrus',
                  'Phaeodactylum_tricornutum',
                  'Nannochloropsis_gaditana',
                  'Ectocarpus_siliculosus',
                  'Ectocarpus_crouaniorum',
                  'Ectocarpus_subulatus',
                  'Ectocarpus_fasciculatus',
                  'Scytosiphon_lomentaria',
                  'Porterinema_fluviatile',
                  'Nemacystus_decipiens',
                  'Cladosiphon_okamuranus',
                  'Laminarionema_elsbetiae',
                  'Saccharina_japonica',
                  'Undaria_pinnatifida']

LAMINARIONEMA_E = 'Laminarionema_elsbetiae'

# ### Class instances ###

BROWN_ALGAE_01 = ['Ectocarpus_fasciculatus_m', 'Undaria_pinnatifida_Kr2015', 'Desmarestia_herbacea_m',
                  'Ectocarpus_siliculosus_m', 'Chordaria_linearis','Scytosiphon_promiscuus_MALE',
                  'Cladosiphon_okamuranus', 'Pleurocladia_lacustris', 'Ectocarpus_crouaniorum_m',
                  'Ectocarpus_siliculosus', 'Ectocarpus_subulatus','Fucus_serratus_MALE', 'Saccharina_latissima_FEMALE',
                  'Dictyota_dichotoma_m', 'Nemacystus_decipiens', 'Porterinema_fluviatile', 'Laminarionema_elsbetiae',
                  'Saccharina_japonica']

R01 = Reactions(DATA_FILE_01, BROWN_ALGAE_01, prio=("Dictyota_dichotoma_m", "Desmarestia_herbacea_m"))
# R40 = Reactions(DATA_FILE_40, BROWN_ALGAE_40)
# RA0 = Reactions(DATA_FILE_A0)
# RA1 = Reactions(DATA_FILE_A1)
# RA2 = Reactions(DATA_FILE_A2)

reac_lostA = reactions_from_file(DATA_LELSB_LOSSES)


# ### Laminarionema loss ###

# print(R40.reactions_loss[LAMINARIONEMA_E])
# print(R01.reactions_loss[LAMINARIONEMA_E])
# print(RA0.reactions_loss[LAMINARIONEMA_E])
# print(RA1.reactions_loss[LAMINARIONEMA_E])
# print(RA2.reactions_loss[LAMINARIONEMA_E])


# ### Common Reactions ###

# print(Reactions.get_common_reactions([R01, R40, RA0], LAMINARIONEMA_E, output_file=None))
# print(Reactions.get_common_reactions([R01, R40, RA1], LAMINARIONEMA_E, output_file=None))
# print(Reactions.get_common_reactions([R01, R40, RA2], LAMINARIONEMA_E, output_file=None))


# ### reactions lost percentage (based on highly shared reactions)

# for k, v in R01.reactions_loss.items():
#     print(k, " : ", round((v[0]/R01.nb_reactions)*100, 3), "%")

# ### genes assoc ###

# print(R01.get_genes_assoc(LAMINARIONEMA_E,
#                           Reactions.get_common_reactions([R01, R40, RA2], LAMINARIONEMA_E)[1],
#                           output_file=True))

reac_list = set(R01.reactions_list)

with open("data/run01_reactions.tsv", "r") as f, open("outputs/cut_run01_reactions.tsv", "w") as o:
    for line in f:
        l = line.split("\t")
        if l[0] in reac_list or l[0] == "reaction":
            o.write(line)
