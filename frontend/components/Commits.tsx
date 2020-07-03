import { Flex, Text } from "@chakra-ui/core";
import React, { ReactElement } from "react";
import CommitsCharts from "@/components/CommitsCharts";

export default function Commits(): ReactElement {
  return (
    <>
      <Flex flexDirection="column" width="60vw">
        <Text fontSize="xl">When do I make commits?</Text>
        <Text>
          I was curious about my own working habits, so here is a breakdown of
          what time of the day and which day of the week I tend to make commits.{" "}
          <Text as="u">Since I started using GitHub.</Text>
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
        <CommitsCharts type={"hours"} />
        <CommitsCharts type={"days"} />
      </Flex>
    </>
  );
}
