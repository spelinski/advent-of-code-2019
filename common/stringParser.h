//
// Created by rohk on 11/30/2019.
//

#ifndef ADVENT_OF_CODE_2019_STRINGPARSER_H
#define ADVENT_OF_CODE_2019_STRINGPARSER_H

#include <algorithm>
#include <map>
#include <string>

namespace stringParse {

    std::map<char, int> getLetterFrequencies(const std::string& inputString) {
        std::map<char, int> outputMap;
        for(auto letter : inputString) {
            outputMap[letter] += 1;
        }
        return outputMap;
    }

}

#endif //ADVENT_OF_CODE_2019_STRINGPARSER_H
