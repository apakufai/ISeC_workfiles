<?php

class NegotiationSkills {
    // Объявление переменных
    private $understandingOfStyles = 0;
    private $adaptation = 0;
    private $compromise = 0;
    private $bidding = 0;
    private $rivalry = 0;
    private $logicArgument = 0;
    private $emotionsArgument = 0;
    private $strengthInstallation = 0;
    private $manipulationInstallation = 0;
    private $negotiationsInstallation = 0;
    private $cooperation = 0;
    private $avoidance = 0;

    // Метод для увеличения значения переменной
    public function increaseSkill($skillName, $value) {
        if (property_exists($this, $skillName)) {
            $this->$skillName += $value;
        } else {
            throw new Exception("Skill '$skillName' does not exist.");
        }
    }

    // Метод для получения текущего значения переменной
    public function getSkillValue($skillName) {
        if (property_exists($this, $skillName)) {
            return $this->$skillName;
        } else {
            throw new Exception("Skill '$skillName' does not exist.");
        }
    }
}

// Пример использования класса
$negotiationSkills = new NegotiationSkills();

// Увеличиваем значение некоторых переменных
$negotiationSkills->increaseSkill('adaptation', 5);
$negotiationSkills->increaseSkill('compromise', 3);

// Получаем значения переменных
echo "Adaptation: " . $negotiationSkills->getSkillValue('adaptation') . "\n"; // Вывод: Adaptation: 5
echo "Compromise: " . $negotiationSkills->getSkillValue('compromise') . "\n"; // Вывод: Compromise: 3
echo "Understanding of Styles: " . $negotiationSkills->getSkillValue('understandingOfStyles') . "\n"; // Вывод: Understanding of Styles: 0

/* 
Описание класса:
Переменные: Все переменные инициализируются значением 0.

Методы:
increaseSkill($skillName, $value): Увеличивает значение указанной переменной на заданное число. Если переменная не существует, выбрасывается исключение.
getSkillValue($skillName): Возвращает текущее значение указанной переменной. Если переменная не существует, выбрасывается исключение.

Пример использования:
В примере показано, как создать объект класса NegotiationSkills, увеличить значения некоторых переменных и получить их текущие значения.
*/

?>
