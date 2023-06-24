import configs from "../configs/configs";
import { ProposalFields } from "../types";
import axios from "axios";

export const getForm = async (): Promise<ProposalFields> => {
  const url = new URL(configs.API_URL + "/proposal_fields");

  const { data } = await axios.get<ProposalFields>(url.toString());

  return data;
};
