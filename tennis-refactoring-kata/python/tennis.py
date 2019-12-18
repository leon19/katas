from itertools import permutations


class Player:
    ONE_POINT = 1
    TWO_POINTS = 2
    FOUR_POINTS = 4

    def __init__(self, name: str) -> None:
        self._name = name
        self._points = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def points(self) -> int:
        return self._points

    def won_point(self) -> None:
        self._points += 1

    def is_tied_with(self, player: "Player") -> bool:
        return self._points == player._points

    def has_advantage_over(self, player: "Player") -> bool:
        return (self._is_last_point() or player._is_last_point()) and self._points - player._points == self.ONE_POINT

    def has_won_against(self, player: "Player") -> bool:
        return self._is_last_point() and self._points - player._points >= self.TWO_POINTS

    def _is_last_point(self) -> bool:
        return self._points >= self.FOUR_POINTS


class ScoreMessageFactory:
    NO_POINTS = 0
    FIFTEEN_POINTS = 1
    THIRTY_POINTS = 2
    FORTY_POINTS = 3

    def get_draw_message(self, points) -> str:
        if points >= 3:
            return "Deuce"

        score = self._get_player_score(points)

        return f"{score}-All"

    def get_score_message(self, player_one_points: int, player_two_points: int) -> str:
        player_one_score = self._get_player_score(player_one_points)
        player_two_score = self._get_player_score(player_two_points)

        return f"{player_one_score}-{player_two_score}"

    def get_advantage_message(self, player_name: str) -> str:
        return "Advantage " + player_name

    def get_win_message(self, player_name: str) -> str:
        return "Win for " + player_name

    def _get_player_score(self, points: int) -> str:
        if points == self.NO_POINTS:
            return "Love"

        if points == self.FIFTEEN_POINTS:
            return "Fifteen"

        if points == self.THIRTY_POINTS:
            return "Thirty"

        if points == self.FORTY_POINTS:
            return "Forty"

        raise ValueError("Invalid score")


class TennisGame1:
    ONE_POINT = 1
    TWO_POINTS = 2
    FOUR_POINTS = 4

    def __init__(self, player_one_name: str, player_two_name: str) -> None:
        self._messages = ScoreMessageFactory()

        self._player_one = Player(player_one_name)
        self._player_two = Player(player_two_name)
        self._players = {player_one_name: self._player_one, player_two_name: self._player_two}

    def won_point(self, player_name: str) -> None:
        self._players[player_name].won_point()

    def score(self) -> str:
        for player, opponent in permutations(self._players.values()):
            if player.is_tied_with(opponent):
                return self._messages.get_draw_message(player.points)

            if player.has_advantage_over(opponent):
                return self._messages.get_advantage_message(player.name)

            if player.has_won_against(opponent):
                return self._messages.get_win_message(player.name)

        return self._messages.get_score_message(self._player_one.points, self._player_two.points)


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
