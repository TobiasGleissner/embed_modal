from common import get_problem_file_list, create_tree
import sys
import filters_for_the_qmltp
from pathlib import Path

class EqualityReplacementResult:
    def __init__(self):
        self.equalityFound = False
        self.inequalityFound = False

def exchangeEqualities(node,eqresult):
    if node.getRule() == "thf_binary_pair":
        operatorNode = node.getChild(1)
        if operatorNode.getContent() == "=":
            eqresult.equalityFound = True
            operatorTerminal = operatorNode.getFirstTerminal()
            operatorTerminal.setContent("@")
            node.addChildFront(Node("terminal","@"))
            node.addChildFront(Node("terminal","customqmltpeq"))
            node.addChildFront(Node("terminal","("))
            node.addChildBack(Node("terminal",")"))
        if operatorNode.getContent() == "!=":
            eqresult.inequalityFound = True
            operatorTerminal = operatorNode.getFirstTerminal()
            operatorTerminal.setContent("@")
            node.addChildFront(Node("terminal","@"))
            node.addChildFront(Node("terminal","customqmltpeqfromineq"))
            node.addChildFront(Node("terminal","("))
            node.addChildBack(Node("terminal",")"))
            node.addChildFront(Node("terminal","~"))
            node.addChildFront(Node("terminal","("))
            node.addChildBack(Node("terminal",")"))

def getIIOTypeDeclaration(identifier):
    return "thf(typedecl_" + identifier + ",type," + identifier + ": ($i > $i > $o))."

def getOOOTypeDeclaration(identifier):
    return "thf(typedecl_" + identifier + ",type," + identifier + ": ($o > $o > $o))."

def main(qmltp_dir, out_dir):
    sys.setrecursionlimit(1500)
    qmltp_path = Path(qmltp_dir)
    out_path = Path(out_dir)
    problem_file_list = get_problem_file_list(qmltp_path)
    problem_white_filter = filters_for_the_qmltp.qmltp_problems_containing_equality_with_axiomatization
    problem_black_filter = None

    for f in problem_file_list:
        if problem_white_filter != None and not f.name in problem_white_filter:
            continue
        if problem_black_filter != None and f.name in problem_black_filter:
            continue
        outFileDir = out_path / f.name[:3]
        outFilePath = outFileDir / f.name
        if outFilePath.exists():
            print(f,"already exists.")
            continue # for an interruptible program
        print("now processing",f)
        with open(f,"r") as fh:
            content = fh.read()
            root = create_tree(content)
            eqresult = EqualityReplacementResult()
            root.dfs(exchangeEqualities,eqresult)
            newProblem = str(root)
            if eqresult.equalityFound:
                newProblem = getIIOTypeDeclaration("customqmltpeq") + "\n" + newProblem
            if eqresult.inequalityFound:
                newProblem = getIIOTypeDeclaration("customqmltpeqfromineq") + "\n" + newProblem
            outFileDir.mkdir(exist_ok=True)
            with open(outFilePath,"w+") as fhw:
                fhw.write(newProblem)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])