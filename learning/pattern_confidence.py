class PatternConfidence:


    def calculate(self, current_pattern, patterns):

        if not patterns:
            return 0


        matches = []

        for pattern in patterns:

            score = 0


            old_features = pattern["features"]

            new_features = current_pattern["features"]


            for key in new_features:

                if key not in old_features:
                    continue


                if old_features[key] == new_features[key]:

                    score += 1


            similarity = score / len(new_features)


            if similarity >= 0.6:

                matches.append(pattern)



        if not matches:

            return 0



        wins = 0


        for m in matches:

            if m["profit_loss"] > 0:

                wins += 1



        confidence = (

            wins / len(matches)

        ) * 100



        return round(confidence,2)