# /deploy-fte
<!-- Slash commands: .md files in commands/. Being replaced by Skills — skills are model-invoked (automatic), commands are user-invoked (manual). [Book: Ch.3] -->
 
Deploy the current Digital FTE to staging.
Use $ARGUMENTS for target override.
 
1. Run evals — abort if any fail
<!-- Evals before deploy. Always. [Book: Ch.47] -->
2. Build Docker image and push
3. Deploy via ArgoCD
4. Run smoke tests
5. Post results to #deployments Slack