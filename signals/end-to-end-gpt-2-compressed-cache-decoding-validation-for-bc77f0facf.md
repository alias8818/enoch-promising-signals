# End-to-end GPT-2 compressed-cache decoding validation for exact-anchor clustered KV compression

Status: `useful_signal`
Project ID: `end-to-end-gpt-2-compressed-cache-decoding-validation-for-bc77f0facf`
Run ID: `end-to-end-gpt-2-compressed-cache-decoding-validation-for-bc77f0facf-20260519T072804676478+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0df6739cebff

## What looked useful

Exact-anchor clustered retention improved teacher-forced top-1 agreement over recent-window controls at every retention level tested: 0.492 vs 0.094 at 25%, 0.766 vs 0.258 at 50%, 0.953 vs 0.633 at 75%, and 0.992 vs 0.852 at 90%. However, greedy full-output match was 0% at 25% and 50%, 25% at 75%, and only 75% at 90%, so the tested method is not an exact or robust compressed-cache decoder at practical compression.

## Boundaries and scale limits

Only GPT-2-small was tested, with 4 prompts, 192-token contexts, 32 generated tokens, greedy decoding, and an unweighted exact-anchor/drop-nonanchor cache. No long-context, large-model, sampling, task-accuracy, or modified attention-kernel validation was run.

## Claim scope

A controlled GPT-2-small test with real Hugging Face KV caches, four 192-token prompt contexts, and 32-token greedy decoding shows that exact-anchor clustered cache retention is better than same-size recent-window retention but does not preserve full-cache end-to-end decoding at useful compression ratios.

## Why it stopped

No-paper closure: this Tier 1 direct GPT-2-small validation found a useful mechanism signal but also showed end-to-end greedy decoding divergence at practical compression levels, so the result is not paper-positive.

## Recommended next action

Run a medium direct follow-up that adds cluster-mass-aware attention or value aggregation and compares against the same exact-anchor and recent-window controls on at least 32 prompts with longer contexts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mass-aware exact-anchor clustered KV cache decoding on GPT-2-small
- Success threshold: At 2x compression, mass-aware exact-anchor clustered decoding should achieve at least 0.95 teacher-forced top-1 agreement and at least 0.80 full 32-token greedy match rate, while beating same-size recent-window and unweighted exact-anchor controls.
- Stop condition: Stop if 2x compression remains below 0.80 teacher-forced top-1 agreement or below 0.50 full greedy match rate on the expanded prompt suite, because that would indicate the mechanism is not robust enough for medium-scale escalation.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-gpt-2-compressed-cache-decoding-validation-for-bc77f0facf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
