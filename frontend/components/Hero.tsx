import { Flex, Text } from "@chakra-ui/core";
import React, { ReactElement } from "react";
import PropTypes from "prop-types";
import styled from "@emotion/styled";

interface Props {
  title: string;
}

const TextStyled = styled(Text)`
  font-family: "Arvo", serif;
  font-weight: 700;
`;

export const Hero = ({ title }: Props): ReactElement => (
  <Flex
    flexDirection="column"
    justifyContent="center"
    alignItems="center"
    height="30vh"
  >
    <TextStyled fontSize={["3xl", "6xl"]}>{title}</TextStyled>
  </Flex>
);

Hero.propTypes = {
  title: PropTypes.string.isRequired,
};
