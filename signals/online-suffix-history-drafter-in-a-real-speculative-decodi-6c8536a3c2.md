# Online suffix-history drafter in a real speculative decoding loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `online-suffix-history-drafter-in-a-real-speculative-decodi-6c8536a3c2`
Run ID: `online-suffix-history-drafter-in-a-real-speculative-decodi-6c8536a3c2-20260519T093134178510+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f42690e0b52a

## What looked useful

The mechanism works in a direct small speculative decoding loop: exact target equality was preserved while repeated suffixes supplied accepted drafts. The ablation shows the expected tradeoff between match frequency and precision as suffix length changes.

## Boundaries and scale limits

Single small target model, 8 hand-controlled prompts, 48 generated tokens per prompt, greedy decoding only, no production KV-cache serving path, no broad corpus, no batching, no learned drafter comparison.

## Claim scope

In a controlled Tier 1 run on distilgpt2 with 8 repetitive structured prompts and greedy decoding, an online suffix-history drafter in a real speculative verification loop exactly matched target greedy output and reduced target forward calls by 50.00% overall at suffix_len=8,max_draft=4; suffix lengths 4, 16, and 32 also preserved exact output and reduced calls by 58.85%, 44.27%, and 26.30%.

## Why it stopped

No-paper closure: the Tier 1 direct test supports the mechanism, but evidence is limited to one small model and controlled repetitive prompts, so it is useful signal rather than publication-grade validation.

## Recommended next action

Run a bounded KV-cache-backed comparison against prompt-lookup decoding and a simple n-gram baseline on a mixed repetitive/non-repetitive prompt suite before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache suffix-history speculative decoding on mixed prompt strata
- Success threshold: Exact greedy equality on all prompts; at least 20% target-call reduction on repetitive strata; no more than 5% wall-clock/token regression on non-repetitive strata; suffix-history beats or ties prompt-lookup and n-gram baselines on target calls/token in at least two model sizes.
- Stop condition: Stop if exact greedy equality fails, if repetitive-stratum target-call reduction is below 20% in both tested model sizes, or if non-repetitive prompts show more than 5% wall-clock/token regression after basic implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/online-suffix-history-drafter-in-a-real-speculative-decodi-6c8536a3c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
