//
// Created by rohk on 11/30/2019.
//

#include "fileParser.h"
#include <iostream>
<<<<<<< HEAD
#include <vector>

int findFuelNeededForWeight(int moduleWeight) {
    return ((moduleWeight / 3) - 2);
}

int findFuelNeededAllModulesIgnoreFuelWeight(const std::vector<int> &changes) {
    int sum = 0;
    for (auto moduleWeight : changes) {
        sum += findFuelNeededForWeight(moduleWeight);
    }
    return sum;
}

int findFuelNeededAllModulesWithFuelWeight(const std::vector<int> &changes) {
    int sum = 0;
    for (auto moduleWeight : changes) {
        int currentFuelNeeded = findFuelNeededForWeight(moduleWeight);
        while (currentFuelNeeded > 0) {
            sum += currentFuelNeeded;
            currentFuelNeeded = findFuelNeededForWeight(currentFuelNeeded);
        }
    }
    return sum;
}

int main() {
    std::vector<int> allChanges = fileParse::storeEachWord<int>("./challenges/challenge1/input.txt");
    std::cout << "Fuel needed all modules: " << findFuelNeededAllModulesIgnoreFuelWeight(allChanges) << "\n";
    std::cout << "Fuel needed all modules and all fuel: " << findFuelNeededAllModulesWithFuelWeight(allChanges) << "\n";
    return 0;
}
=======
#include <iterator>
#include <numeric>
#include <set>
#include <vector>

int findSumSeenTwice(const std::vector<int>& changes) {
    std::set<int> sumsHit = {0};
    auto it = changes.begin();
    int sum = 0;
    while(true) {
        if(it == changes.end()) { it = changes.begin(); }
        sum += *it;
        ++it;
        if(sumsHit.find(sum) != sumsHit.end()) {
            return sum;
        }
        sumsHit.insert(sum);
    }
    return 0;
}

int main(){
    std::vector<int> allChanges = fileParse::storeEachWord<int>("./challenges/challenge1/input.txt");

    std::cout << "Sum of Numbers: " << std::accumulate(allChanges.begin(), allChanges.end(), 0) << "\n";
    std::cout << "Sum seen twice: " << findSumSeenTwice(allChanges) << "\n";
    return 0;
}
>>>>>>> d0b287d... test challenge1
