import { useQuery } from "@tanstack/vue-query";
import { getFields, getOperadoras } from "@/services/operadoras";

export const useData = () => {
  return useQuery({
    queryKey: ["operadoras"],
    queryFn: getOperadoras,
  });
};

export const useFields = () => {
  return useQuery({
    queryKey: ["fields"],
    queryFn: getFields,
  });
};
