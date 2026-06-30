# Live Small-LM Verification of Adaptive Verified-Output N-Gram Speculative Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-small-lm-verification-of-adaptive-verified-output-n-g-40f55bb1a3`
Run ID: `live-small-lm-verification-of-adaptive-verified-output-n-g-40f55bb1a3-20260527T091503203551+0000`

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

- Parent run decision: Adaptive N-Gram Speculative Cache from Verified Outputs: enoch://control-plane/projects/adaptive-n-gram-speculative-cache-from-verified-outputs-b9db1ebe9020/runs/adaptive-n-gram-speculative-cache-from-verified-outputs-b9db1ebe9020-20260526T042100915245+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f8722ba9e610

## What looked useful

The verified-output n-gram mechanism cleared the Tier 1 direct threshold on a real small LM: exact baseline match, substantial target-forward reduction, and proposal acceptance above threshold. The adaptive policy component remains unsupported because the no-adaptive ablation was essentially tied and slightly better.

## Boundaries and scale limits

Small curated repetition-friendly prompt set; 512 generated target tokens total; full-context CPU harness rather than production KV-cache serving; greedy decoding only; no larger models, broad corpora, sampling, concurrency, or adversarial prompt robustness tested.

## Claim scope

On a controlled 8-prompt distilgpt2 greedy-decoding test, a verified-output n-gram speculative cache exactly preserved target output while reducing target forward calls by 58.4% with 68.7% proposal-token acceptance. The simple adaptive chooser did not outperform a fixed n-gram selection ablation.

## Why it stopped

No-paper useful signal: the mechanism worked in a small direct test, but the evidence is narrow and curated, and the adaptive component did not beat the fixed-rule ablation.

## Recommended next action

Run a medium direct validation on GPT-2-small-class or comparable models with a natural held-out prompt corpus, a KV-cache-aware verifier implementation, and baselines for fixed n-gram lookup, no cache, and prompt-lookup drafting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Corpus KV-Cache Validation of Verified-Output N-Gram Speculative Decoding
- Success threshold: Across at least 50 natural prompts and 6400 generated tokens, exact output match on all prompts, at least 20% wall-latency reduction versus no-cache greedy decoding, at least 25% target-forward reduction, and adaptive selection at least 5% relative better than fixed n-gram selection on either accepted tokens per verifier call or wall latency.
- Stop condition: Stop as unsupported if exact output diverges once, if forward reduction is below 10%, if wall latency does not improve, or if adaptive selection remains tied with or worse than fixed n-gram selection.

## Evidence references

- Artifact root: `<local-path>/projects/live-small-lm-verification-of-adaptive-verified-output-n-g-40f55bb1a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
