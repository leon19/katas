class TennisGame1:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_points = 0
        self.player_two_points = 0

    def won_point(self, player_name):
        if player_name == self.player_one_name:
            self.player_one_points += 1
        else:
            self.player_two_points += 1

    def score(self):
        if self._is_draw():
            return {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}.get(self.player_one_points, "Deuce")

        if self.player_one_points >= 4 or self.player_two_points >= 4:
            minus_result = self.player_one_points - self.player_two_points

            if minus_result == 1:
                return self._get_advantage_message(self.player_one_name)

            if minus_result == -1:
                return self._get_advantage_message(self.player_two_name)

            if minus_result >= 2:
                return self._get_win_message(self.player_one_name)

            return self._get_win_message(self.player_two_name)

        player_one_score = self._get_player_score(self.player_one_points)
        player_two_score = self._get_player_score(self.player_two_points)

        return f"{player_one_score}-{player_two_score}"

    def _is_draw(self):
        return self.player_one_points == self.player_two_points

    def _get_player_score(self, points):
        if points == 0:
            return "Love"

        if points == 1:
            return "Fifteen"

        if points == 2:
            return "Thirty"

        if points == 3:
            return "Forty"

        raise ValueError("Invalid score")

    def _get_advantage_message(self, player_name):
        return "Advantage " + player_name

    def _get_win_message(self, player_name):
        return "Win for " + player_name


class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        if self.p1points == self.p2points and self.p1points < 3:
            if self.p1points == 0:
                result = "Love"
            if self.p1points == 1:
                result = "Fifteen"
            if self.p1points == 2:
                result = "Thirty"
            result += "-All"
        if self.p1points == self.p2points and self.p1points > 2:
            result = "Deuce"

        P1res = ""
        P2res = ""
        if self.p1points > 0 and self.p2points == 0:
            if self.p1points == 1:
                P1res = "Fifteen"
            if self.p1points == 2:
                P1res = "Thirty"
            if self.p1points == 3:
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:
                P2res = "Fifteen"
            if self.p2points == 2:
                P2res = "Thirty"
            if self.p2points == 3:
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p1points < 4:
            if self.p1points == 2:
                P1res = "Thirty"
            if self.p1points == 3:
                P1res = "Forty"
            if self.p2points == 1:
                P2res = "Fifteen"
            if self.p2points == 2:
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if self.p2points > self.p1points and self.p2points < 4:
            if self.p2points == 2:
                P2res = "Thirty"
            if self.p2points == 3:
                P2res = "Forty"
            if self.p1points == 1:
                P1res = "Fifteen"
            if self.p1points == 2:
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = "Advantage " + self.player1Name

        if self.p2points > self.p1points and self.p1points >= 3:
            result = "Advantage " + self.player2Name

        if self.p1points >= 4 and self.p2points >= 0 and (self.p1points - self.p2points) >= 2:
            result = "Win for " + self.player1Name
        if self.p2points >= 4 and self.p1points >= 0 and (self.p2points - self.p1points) >= 2:
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1


class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1) else "Win for " + s
