# Self-Speculative Decoding with Draft-Only Early Exit Layers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `self-speculative-decoding-with-draft-only-early-exit-layers-3622720c4b7e`
Run ID: `self-speculative-decoding-with-draft-only-early-exit-layers-3622720c4b7e-20260608T154153550420+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/75bbb8f75b39

## What looked useful

Across three seeds, draft-only adapter agreement with the final verifier averaged 22.5% argmax and 47.0% top-3, compared with 12.6%/30.4% for a simple auxiliary early exit and 1.9%/4.9% for an untrained early-exit head.

## Boundaries and scale limits

Synthetic deterministic sequence data, 4-layer randomly initialized Transformer, 3 seeds, 1200 training steps per variant, no pretrained LM, no natural-language benchmark, no end-to-end speculative decoding speed measurement.

## Claim scope

In a tiny synthetic causal-Transformer task, a draft-only adapter attached after layer 2 improved verifier argmax agreement over both an untrained early-exit head and an auxiliary-trained early-exit head.

## Why it stopped

Stopped after a reproducible synthetic/proxy useful signal; this is not full validation of self-speculative decoding speedup or quality on natural language models.

## Recommended next action

Run a bounded GPT-2-small-class pretrained-model follow-up measuring accepted tokens per verifier pass, tokens/sec, perplexity retention, and adapter overhead against auxiliary-exit and no-exit controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Draft-only early exits on GPT-2-small self-speculative decoding
- Success threshold: At least 1.25x end-to-end decode tokens/sec over no-speculation and at least 15% higher accepted-token rate than an auxiliary early-exit head, with no measurable verifier perplexity regression.
- Stop condition: Stop if accepted-token rate does not beat the auxiliary-exit control by at least 5% absolute or if adapter overhead erases speedup in a 200-sample decode benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-with-draft-only-early-exit-layers-3622720c4b7e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
