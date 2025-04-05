<script setup>
import { useData } from "@/hooks/useData";
import { DataTable } from "primevue";
import { ref, watch } from "vue";
const { data: rawData, isLoading, isError, error } = useData();

const data = ref([]);

const date_formater = (dateStr) => {
    const date = new Date(dateStr);
    return date.toLocaleDateString("pt-BR", {
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
    });
}

const cnpj_formater = (cnpj) =>
  cnpj.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, "$1.$2.$3/$4-$5");

watch(rawData, (dataFetched) => {

  data.value = dataFetched.map((item) => {
    return {
      Registro: item.REG_ANS,
      CNPJ: cnpj_formater(item.CNPJ),
      Razao_Social: item.RAZAO_SOCIAL,
      Data_Registro: date_formater(item.DATA_REGISTRO_ANS),
      Nome_Fantasia: item.NOME_FANTASIA,
      Modalidade: item.MODALIDADE,
      Cidade_UF: `${item.CIDADE} - ${item.UF}`,
      Telefone: `${
        item.TELEFONE ? `(${item.DDD}) ${item.TELEFONE}` : "Não informado"
      }`,
      Email: `${item.EMAIL ? item.EMAIL.toLowerCase() : "Não informado"}`,
      Representante: item.REPRESENTANTE,
      Cargo_Representante: item.CARGO_REPRESENTANTE,
    };
  });
});

const columns = [
  { field: "Registro", header: "Registro ANS" },
  { field: "CNPJ", header: "CNPJ" },
  { field: "Razao_Social", header: "Razão Social" },
  { field: "Data_Registro", header: "Data Registro ANS" },
  { field: "Nome_Fantasia", header: "Nome Fantasia" },
  { field: "Modalidade", header: "Modalidade" },
  { field: "Cidade_UF", header: "Cidade" },
  { field: "Telefone", header: "Telefone" },
  { field: "Email", header: "Email" },
  { field: "Representante", header: "Representante" },
  { field: "Cargo_Representante", header: "Cargo" },
];
</script>

<template>
  <Panel header="Operadoras" class="items-center justify-center align-center">
    <ProgressSpinner v-if="isLoading" />
    <DataTable
      v-if="!isLoading"
      :size="small"
      :value="data"
      :loading="isLoading"
      :virtualScrollerOptions="{ itemSize: 50 }"
      scrollable
      scrollHeight="86vh"
      resizableColumns
      columnResizeMode="expand"
    >
      <Column v-for="col in columns" :field="col.field" :header="col.header"/>
    </DataTable>
  </Panel>
</template>
