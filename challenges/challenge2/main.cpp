//
// Created by rohk on 11/30/2019.
//

#include "fileParser.h"
#include <iostream>
#include <regex>
#include <vector>

std::vector<int> getAllRegisters(std::string program)
{
    std::vector<int> output;
    std::stringstream ss(program);
    for(int i; ss >> i;)
    {
        output.push_back(i);
        if(ss.peek() == ',')
        {
            ss.ignore();
        }
    }
    return output;
}

enum OpCode {
    add = 1,
    multiply = 2,
    end = 99
};

std::vector<int> runProgram(std::vector<int> inputState)
{
    std::vector<int> programState = inputState;
    int currentOpCodeLoc = 0;
    int currentOpCode = programState[currentOpCodeLoc];
    while(currentOpCode != OpCode::end)
    {
        if(currentOpCode == OpCode::add)
        {
            int leftLocation = programState[currentOpCodeLoc+1];
            int rightLocation = programState[currentOpCodeLoc+2];
            int storageLocation = programState[currentOpCodeLoc+3];

            int leftValue = programState[leftLocation];
            int rightValue = programState[rightLocation];
            programState[storageLocation] = leftValue + rightValue;
        }
        else if(currentOpCode == OpCode::multiply)
        {
            int leftLocation = programState[currentOpCodeLoc+1];
            int rightLocation = programState[currentOpCodeLoc+2];
            int storageLocation = programState[currentOpCodeLoc+3];

            int leftValue = programState[leftLocation];
            int rightValue = programState[rightLocation];
            programState[storageLocation] = leftValue * rightValue;

        }
        else
        {
            std::cout << "An error occured in op code at location: " << currentOpCodeLoc << "\n";
            break;
        }
        currentOpCodeLoc += 4;
        currentOpCode = programState[currentOpCodeLoc];
    }

    return programState;

}

int findNounVerbAnswerBruteForce(std::vector<int> inputState, int targetValue)
{
    int noun = 0;
    int verb = -1;
    std::vector<int> currentState;
    do{
        currentState = inputState;
        if(noun == 99 && verb == 99){
            std::cout << "An error occured trying to find noun and verb\n";
            break;
        } else if(verb == 99) {
            noun += 1;
            verb = 0;
        }
        else{
            ++verb;
        }
        currentState[1] = noun;
        currentState[2] = verb;
        currentState = runProgram(currentState);
    }while(currentState[0]!=targetValue);
    return (100 * noun) + verb;
}

int main() {
    std::vector<std::string> allLines = fileParse::storeEachLine("./challenges/challenge2/input.txt");
    std::vector<int> allRegisters = getAllRegisters(allLines[0]);
    std::vector<int> finalState = runProgram(allRegisters);
    std::cout << "Final state part 1 is: ";
    for(int value : finalState)
    {
        std::cout << value << ",";
    }
    std::cout << "\n";

    std::cout << "Noun verb multiple is: " << findNounVerbAnswerBruteForce(allRegisters, 19690720) << "\n";
    return 0;
}
