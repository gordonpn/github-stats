import { theme as chakraTheme } from "@chakra-ui/core";

const fonts = { ...chakraTheme.fonts, mono: `'Menlo', monospace` };

const breakpoints = ["40em", "52em", "64em"];

const theme = {
  ...chakraTheme,
  colors: {
    ...chakraTheme.colors,
    black: "#504f54",
  },
  fonts,
  breakpoints,
  icons: {
    ...chakraTheme.icons,
  },
};

export default theme;
