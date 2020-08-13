#include <iostream>
#include <vector>
#include <memory>

class Observer
{
protected:
    int excitementLevel;

public:
    Observer()
    {
        this->excitementLevel = 0;
    }

    virtual void update() = 0;
};

class FootballGame
{
private:
    std::vector<Observer *> audiences;

public:
    void reg(Observer *audience)
    {
        this->audiences.push_back(audience);
    }

    void addGoal()
    {
        notify();
    }

    void notify();
};

class YoungAudience : public Observer {
public:
    YoungAudience() : Observer() {
    }

    void update() {
        this->excitementLevel++;
        if (this->excitementLevel > 3) {
            std::cout << "Young: yey, more than 3! it's " << 
                this->excitementLevel << std::endl;
        }
        else {
            std::cout << "Young: hmmm less than 3: " << this->excitementLevel <<
                std::endl;
        }
    }
};

class OldAudience : public Observer {
public:
    OldAudience() : Observer() {
    }

    void update() {
        this->excitementLevel++;
        if (this->excitementLevel > 5) {
            std::cout << "Old: more than 5! it's " << 
                this->excitementLevel << std::endl;
        }
        else {
            std::cout << "Old: hmmm less than 5: " << this->excitementLevel <<
                std::endl;
        }
    }
};

void FootballGame::notify() {
    for (int i = 0; i < audiences.size(); i++) {
        audiences.at(i)->update();
    }
}

int main() {
    auto game = FootballGame();
    auto young1 = YoungAudience();
    auto young2 = YoungAudience();
    auto old = OldAudience();
    game.reg(&young1);
    game.reg(&young2);
    game.reg(&old);
    for (int i = 0; i < 7; i++) {
        game.addGoal();
    }

    return 0;
}
