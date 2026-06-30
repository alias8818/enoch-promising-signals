# Suffix-Tree Drafting with Exact Verification for GPT-2-Small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-drafting-with-exact-verification-for-gpt-2-small-375202aff441`
Run ID: `suffix-tree-drafting-with-exact-verification-for-gpt-2-small-375202aff441-20260608T131019975571+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0fbedae6cd8d

## What looked useful

Exact verification worked for every tested prompt, and suffix-history drafts reduced GPT-2-small target calls by 46.875% on the natural prompt subset and 79.297% on repetitive prompts. This supports the mechanism but not a paper-ready or production-speed claim.

## Boundaries and scale limits

Small local prompt set; hand-written natural prompts plus synthetic repetitive prompts; full-context forward-pass baseline rather than optimized KV-cache serving; naive suffix search rather than optimized suffix-tree data structure.

## Claim scope

On 12 short local prompts with 64-token greedy GPT-2-small generation, a suffix-history drafter with exact argmax verification preserved exact greedy output and reduced target-model forward calls from 768 to 325 overall; the effect was strongest on repetitive prompts.

## Why it stopped

Proxy/local validation only: exactness and target-call reduction were directly tested, but broad-corpus behavior and optimized KV-cache latency were not.

## Recommended next action

Stop this run as a useful no-paper signal; next run should benchmark a KV-cache verifier on a larger held-out text corpus before making any serving-speed or generality claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache suffix-history drafting on held-out GPT-2-small prompts
- Success threshold: All outputs exactly match greedy decoding, target-model step reduction is at least 20%, and median end-to-end latency is no worse than 1.05x greedy KV-cache baseline on the held-out prompt set.
- Stop condition: Stop if exactness fails on any prompt, if target-step reduction is below 10%, or if median latency is worse than 1.20x greedy KV-cache baseline after basic implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-drafting-with-exact-verification-for-gpt-2-small-375202aff441`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
