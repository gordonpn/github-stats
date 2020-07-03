import { Flex, Text } from "@chakra-ui/core";
import React, { ReactElement } from "react";
import CommitsDays from "@/components/CommitsDays";
import CommitsHours from "@/components/CommitsHours";

export default function Commits(): ReactElement {
  return (
    <>
      <Flex flexDirection="column" width="60vw">
        <Text>When do I make commits?</Text>
        <Text>
          I was curious about my own working habits, so here is a breakdown of
          what time of the day I tend to commit and which day of the week I tend
          to make commits. Since I started using GitHub.
        </Text>
      </Flex>
      <Flex
        justifyContent="space-around"
        alignItems="center"
        flexDirection={["column", "row"]}
        width={["90vw", "40vw"]}
        height={["50vh", "25vh"]}
        margin="10vh"
      >
        <CommitsDays />
        <CommitsHours />
      </Flex>
    </>
  );
}
