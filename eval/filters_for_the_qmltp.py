from extract_qmltp_info import extract_qmltp_info_from_problem_file_list_to_dicts
from common import get_problem_file_list

file_list = None
qmltp_info = None
cumul_interesting_problems = None
def init(qmltp_dir):
    file_list = get_problem_file_list(qmltp_dir)
    global qmltp_info
    qmltp_info = extract_qmltp_info_from_problem_file_list_to_dicts(file_list)
    global cumul_interesting_problems
    cumul_interesting_problems = get_different_cumul_status()

def get_different_cumul_status():
    ret = {}
    for problem_name,system_dict in qmltp_info.items():
        for system, quantification_dict in system_dict.items():
            if problem_name in ret:
                continue
            if (quantification_dict["$cumulative"] != "Unsolved"):#and system != "$modal_system_S5":
                if (quantification_dict["$cumulative"] != quantification_dict["$constant"] and quantification_dict["$constant"] != "Unsolved") or \
                    (quantification_dict["$cumulative"] != quantification_dict["$varying"] and quantification_dict["$varying"] != "Unsolved" ):
                    ret[problem_name] = system_dict
    return ret


qmltp_problems_containing_equality = [
    "SYM052+1.p",
    "SYM055+1.p",
    "SYM056+1.p",
    "SYM057+1.p",
    "SYM064+1.p",
    "SYM068+1.p",
    "SYM085+1.p",
    "GSV060+1.p",
    "GSV061+1.p",
    "GSV062+1.p",
    "GSV063+1.p",
    "GSV064+1.p",
    "GSV065+1.p",
    "GSV066+1.p",
    "GSV067+1.p",
    "GSV068+1.p",
    "GSV069+1.p",
    "GSV070+1.p",
    "GSV071+1.p",
    "GSV072+1.p",
    "GSV073+1.p",
    "GSV074+1.p",
    "GSV075+1.p",
    "GSV076+1.p",
    "GSV077+1.p",
    "GSV078+1.p",
    "GSV079+1.p",
    "GSV080+1.p",
    "GSV081+1.p",
    "GSV082+1.P",
    "GSV083+1.p",
    "GSV084+1.p",
    "GSV085+1.p",
    "GSV086+1.p",
    "GSV087+1.p",
    "GSV088+1.p",
    "GSV089+1.p",
    "GSV090+1.p",
    "GSV091+1.p",
    "GSV092+1.p",
    "GSV093+1.p",
    "GSV094+1.p",
    "GSV095+1.p",
    "GSV096+1.p",
    "GSV097+1.p",
    "GSV098+1.p",
    "GSV099+1.p",
    "GSV100+1.p",
    "GSV101+1.p",
    "GSV102+1.p",
    "GSV103+1.p",
    "GSV104+1.p",
    "GSV105+1.p",
    "GSV106+1.p",
    "GSV107+1.p"]

qmltp_problems_without_modal_operators = [
    "NLP001+1.p",
    "NLP002+1.p",
    "NLP003+1.p",
    "NLP004+1.p",
    "NLP005+1.p",
    "SET002+3.p",
    "SET002+4.p",
    "SET008+3.p",
    "SET009+3.p",
    "SET010+3.p",
    "SET011+3.p",
    "SET012+4.p",
    "SET013+4.p",
    "SET014+3.p",
    "SET014+4.p",
    "SET015+4.p",
    "SET016+1.p",
    "SET016+4.p",
    "SET017+1.p",
    "SET018+1.p",
    "SET018+4.p",
    "SET019+4.p",
    "SET020+1.p",
    "SET024+1.p",
    "SET025+1.p",
    "SET027+1.p",
    "SET027+3.p",
    "SET027+4.p",
    "SET043+1.p",
    "SET044+1.p",
    "SET045+1.p",
    "SET046+1.p",
    "SET047+1.p",
    "SET054+1.p",
    "SET055+1.p",
    "SET056+1.p",
    "SET060+1.p",
    "SET061+1.p",
    "SET062+1.p",
    "SET062+3.p",
    "SET062+4.p",
    "SET063+1.p",
    "SET063+3.p",
    "SET063+4.p",
    "SET573+3.p",
    "SET574+3.p",
    "SET575+3.p",
    "SET576+3.p",
    "SET577+3.p",
    "SET578+3.p",
    "SET579+3.p",
    "SET580+3.p",
    "SET581+3.p",
    "SET582+3.p",
    "SET583+3.p",
    "SET900+1.p",
    "SET901+1.p",
    "SET902+1.p",
    "SET903+1.p",
    "SET904+1.p",
    "SET906+1.p",
    "SET907+1.p",
    "SET908+1.p",
    "SET909+1.p",
    "SET910+1.p",
    "SET911+1.p",
    "SET912+1.p",
    "SET913+1.p",
    "SET914+1.p",
    "SET915+1.p",
    "SET916+1.p",
    "SET917+1.p",
    "SET918+1.p",
    "SET919+1.p",
    "SET920+1.p",
    "SET921+1.p",
    "SET923+1.p",
    "SET924+1.p",
    "SET925+1.p",
    "SET926+1.p"
]
