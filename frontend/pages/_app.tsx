import { ColorModeProvider, CSSReset, ThemeProvider } from "@chakra-ui/core";
import { AppProps } from "next/app";
import theme from "src/theme";
import React, { ReactElement } from "react";
import Head from "next/head";

function MyApp({ Component, pageProps }: AppProps): ReactElement {
  return (
    <>
      <Head>
        <title>GitHub Stats</title>
        <meta
          name="description"
          content="Display interesting GitHub profile developer statistics with charts"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Arvo:wght@700&display=swap"
          rel="stylesheet"
        />
        <meta name="monetization" content="$ilp.uphold.com/RKA9rkK4w9PD" />
        <link
          rel="apple-touch-icon"
          sizes="180x180"
          href="/apple-touch-icon.png"
        />
        <link
          rel="icon"
          type="image/png"
          sizes="32x32"
          href="/favicon-32x32.png"
        />
        <link
          rel="icon"
          type="image/png"
          sizes="16x16"
          href="/favicon-16x16.png"
        />
        <link rel="manifest" href="/site.webmanifest" />
        <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#5bbad5" />
        <meta name="msapplication-TileColor" content="#da532c" />
        <meta name="theme-color" content="#ffffff" />
      </Head>
      <ThemeProvider theme={theme}>
        <CSSReset />
        <Component {...pageProps} />
      </ThemeProvider>
    </>
  );
}

export default MyApp;
