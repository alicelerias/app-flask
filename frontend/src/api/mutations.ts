import axios from "axios";

import configs from "./../configs/configs";
import { Responses } from "../types";

export const createResponse = async (input: Responses) => {
  const url = new URL(configs.API_URL + "/proposal");
  await axios.post(url.toString(), input);
};
