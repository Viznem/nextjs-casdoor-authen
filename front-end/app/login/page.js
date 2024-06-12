"use client";
import { useEffect } from "react";
import Sdk from "casdoor-js-sdk";
import sdkConfig from "@/app/conf";

const Login = () => {
  useEffect(() => {
    const CasdoorSDK = new Sdk(sdkConfig);
    CasdoorSDK.signin_redirect();
  }, []);

  return <></>;
};

export default Login;