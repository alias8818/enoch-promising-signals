# Anchor-Conditioned Speculative Drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-conditioned-speculative-drafting-efcbf0d22f53`
Run ID: `anchor-conditioned-speculative-drafting-efcbf0d22f53-20260605T032854029751+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a52a6c210eec

## What looked useful

Across three seeds, correct anchor conditioning raised exact target acceptance from 0.718246 to 0.870248 mean (+0.152002 absolute, +21.16% relative) over 4,644,864 eval tokens per model. Shuffled anchors collapsed acceptance to 0.228209, showing the effect depends on correct anchor information.

## Boundaries and scale limits

Synthetic data only; tiny 2-layer transformers; one-step exact acceptance only; no real pretrained LLM target, no multi-token block verification, no serving latency, and no accounting for anchor acquisition cost.

## Claim scope

In a controlled synthetic sequence process where sparse future anchor tokens encode the latent topic of each segment, a same-size anchor-conditioned draft transformer improves exact one-step speculative acceptance versus a causal-prefix-only draft transformer.

## Why it stopped

No-paper closure: this run supports the mechanism only in a synthetic controlled setting, not a real LLM-serving validation.

## Recommended next action

Run a bounded deepen experiment with a small pretrained target/draft pair and a cheap explicit anchor source, measuring accepted tokens per target call and end-to-end latency against ordinary speculative decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Anchor-Conditioned Speculative Decoding With Cheap Future Keywords
- Success threshold: At least 10% higher accepted tokens per target call than ordinary speculative decoding and non-worse end-to-end latency on the same prompts/model pair, with shuffled anchors removing the gain.
- Stop condition: Stop if correct anchors do not improve accepted tokens per target call by at least 5% over standard speculative decoding or if anchor acquisition overhead eliminates latency gains.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-conditioned-speculative-drafting-efcbf0d22f53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
