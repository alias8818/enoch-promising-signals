# Medusa-Single-Head: Frozen-Base + One Tiny Draft Head

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medusa-single-head-frozen-base-one-tiny-draft-head-a0518b0fa7f1`
Run ID: `medusa-single-head-frozen-base-one-tiny-draft-head-a0518b0fa7f1-20260610T084653404786+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5157dfaf44e2

## What looked useful

Across seeds 1-3, base next-token top-1 accuracy averaged 0.9294 and the single draft head averaged 0.4680 top-1 / 0.6821 top-4 for two-ahead prediction, versus 0.0146 bigram top-1 and 0.0161 unigram top-1 controls. The draft head was 4.80% of base parameters.

## Boundaries and scale limits

Toy synthetic data only; no pretrained LM, natural text, verifier acceptance, latency, multi-head comparison, or production speculative decoding measurement.

## Claim scope

In a synthetic lag-copy autoregressive language, a frozen 520,960-parameter causal Transformer base with one 25,024-parameter MLP draft head can predict token t+2 from hidden state h_t far above unigram and current-token bigram controls across three seeds.

## Why it stopped

Toy proxy supports the frozen-base single-head mechanism but does not directly validate Medusa serving speedup or natural-language LLM behavior.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen test on a GPT-2-small-class or pretrained small LM with actual speculative acceptance and latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Single frozen Medusa draft head on GPT-2-small-class text
- Success threshold: At least 1.15x measured decode throughput improvement or a clearly positive verifier-acceptance/latency tradeoff at matched output quality, with draft parameters under 10% of base parameters.
- Stop condition: Stop if held-out verifier acceptance stays below 20% for top-1 proposals or if measured throughput fails to exceed greedy base decoding after kernel/implementation overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/medusa-single-head-frozen-base-one-tiny-draft-head-a0518b0fa7f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
