{{/*
Expand the name of the chart.
*/}}
{{- define "deploytual.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "deploytual.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "deploytual.labels" -}}
helm.sh/chart: {{ include "deploytual.name" . }}-{{ .Chart.Version }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: deploytual
{{- end }}

{{/*
Selector labels
*/}}
{{- define "deploytual.selectorLabels" -}}
app.kubernetes.io/name: {{ include "deploytual.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
