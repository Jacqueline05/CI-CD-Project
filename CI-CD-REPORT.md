# CI/CD Final Project Submission

## GitHub evidence

| Task | Evidence |
|---|---|
| 1 | [CI/CD Project repository](https://github.com/Jacqueline05/CI-CD-Project) |
| 2 | [GitHub Actions lint step](https://github.com/Jacqueline05/CI-CD-Project/blob/main/.github/workflows/workflow.yml#L26-L27) |
| 3 | [GitHub Actions test step](https://github.com/Jacqueline05/CI-CD-Project/blob/main/.github/workflows/workflow.yml#L29-L30) |
| 4 | [Tekton cleanup task](https://github.com/Jacqueline05/CI-CD-Project/blob/main/.tekton/tasks.yml#L1-L15) |
| 5 | [Tekton nose test task](https://github.com/Jacqueline05/CI-CD-Project/blob/main/.tekton/tasks.yml#L17-L32) |

## OpenShift evidence checklist

The following screenshots must be captured from the live OpenShift console after applying the manifests and running the pipeline. They cannot be generated from GitHub alone.

| Task | Required filename | Capture |
|---|---|---|
| 6 | `oc-pipelines-console-pvc-details.png` | PVC details for `oc-pipelines-console-pvc` |
| 7 | `cicd-github-validate.png` | GitHub Actions workflow completed successfully |
| 8 | `oc-pipelines-oc-final.png` | OpenShift Pipeline details for `ci-cd-pipeline` |
| 9 | `oc-pipelines-oc-green.png` | Successful OpenShift PipelineRun |
| 10 | `oc-pipelines-app-logs.png` | Running application logs from the OpenShift console |

## Deployment files

- [Tekton tasks](.tekton/tasks.yml)
- [Tekton pipeline](.tekton/pipeline.yml)
- [PVC manifest](openshift/pvc.yml)
- [Application, Service, and Route](openshift/app.yml)
