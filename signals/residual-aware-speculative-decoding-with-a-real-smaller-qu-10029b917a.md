# Residual-Aware Speculative Decoding with a Real Smaller Quantized Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-aware-speculative-decoding-with-a-real-smaller-qu-10029b917a`
Run ID: `residual-aware-speculative-decoding-with-a-real-smaller-qu-10029b917a-20260524T040603284653+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: End-to-End Residual-Aware Speculative Decoding with a Quantized Draft Model: enoch://control-plane/projects/end-to-end-residual-aware-speculative-decoding-with-a-quan-bc4132a403/runs/end-to-end-residual-aware-speculative-decoding-with-a-quan-bc4132a403-20260524T032443023833+0000
- Parent run decision: Residual-Aware Speculative Decoding: Using Quantization Residuals to Improve Draft Acceptance: enoch://control-plane/projects/residual-aware-speculative-decoding-using-quantization-residuals-to-improve-draft-acceptance-156f8494ee2c/runs/residual-aware-speculative-decoding-using-quantization-residuals-to-improve-draft-acceptance-156f8494ee2c-20260524T031345599389+0000

## What looked useful

Residual-aware speculative decoding with a quantized smaller draft was exact against target greedy and improved confirmation-run acceptance from 0.832520 to 0.841797, reducing target calls/token from 0.333984 to 0.327148. A global residual control achieved 0.840332 acceptance and 0.328125 target calls/token, so most of the effect is global logit-bias correction rather than context-specific residual awareness.

## Boundaries and scale limits

Tested only GPT-2/distilGPT2, greedy decoding, fixed local prompt sets, 64-128 generated tokens per prompt, and dequantized int8-perturbed draft weights rather than packed int8 serving kernels. Not evidence for 7B+ models, sampling, production throughput, or broad benchmark robustness.

## Claim scope

On GPT-2 target greedy decoding with a real smaller DistilGPT2 draft whose weights were symmetrically int8-quantized and dequantized for inference, residual logit correction preserved exact target-greedy outputs and slightly improved speculative acceptance/target-call metrics over vanilla on fixed medium prompt sets. The context-keyed residual mechanism itself was not strongly supported because a global residual control matched almost all of the gain.

## Why it stopped

Tier 2 direct evidence found only a small efficiency improvement, and the stronger mechanism claim is weakened by a global residual control that captures nearly all of the benefit.

## Recommended next action

Stop this run as no-paper useful signal; if deepened, test whether context-keyed residuals beat a global residual baseline by at least 3% target-call reduction on multiple target/draft model pairs and a broader prompt suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Context-Keyed Residuals Versus Global Bias Across Multiple Draft/Target Pairs
- Success threshold: Context-keyed residual correction must reduce target calls/token by at least 3% relative to global residual on both model pairs while preserving exact target-greedy outputs.
- Stop condition: Stop if context-keyed residuals fail to beat global residual by 3% target-calls/token on either model pair or if exact target-greedy equivalence fails.

## Evidence references

- Artifact root: `<local-path>/projects/residual-aware-speculative-decoding-with-a-real-smaller-qu-10029b917a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
