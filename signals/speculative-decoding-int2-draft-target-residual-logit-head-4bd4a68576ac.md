# Speculative decoding: INT2 draft + target residual logit head

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-decoding-int2-draft-target-residual-logit-head-4bd4a68576ac`
Run ID: `speculative-decoding-int2-draft-target-residual-logit-head-4bd4a68576ac-20260621T034012229189+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ad6e7f5c06bf

## What looked useful

The mechanism is worth a bounded real-model follow-up: residual logit correction consistently improved distribution overlap and expected acceptance after INT2 draft-head quantization in the local proxy, with rank 8 recovering about 75.6% of the gap on the three-seed sweep.

## Boundaries and scale limits

No real transformer, no actual speculative decoding loop, no latency measurement, no tokenizer-scale vocabulary, no KV-cache/batching effects, and no hardware INT2 kernel. CPU-only NumPy runs on small synthetic vocab 128 and hidden 64.

## Claim scope

Synthetic autoregressive logit-head proxy only: an INT2 draft output head plus a rank-8 target-side residual logit head recovered 69.19% of the dense-vs-INT2 expected speculative-acceptance gap in the primary run, and rank sweeps across three seeds showed monotonic recovery.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only despite supporting the mechanism.

## Recommended next action

Run a bounded real-transformer follow-up with a small target/draft pair, true speculative decoding acceptance, and latency-normalized throughput before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer validation of INT2 draft residual logit head
- Success threshold: INT2 plus residual recovers at least 50% of dense-vs-INT2 acceptance loss and achieves at least 1.05x throughput over the dense draft baseline at matched output quality on the bounded real-model test.
- Stop condition: Stop if the residual variant fails to recover 30% of acceptance loss or if measured residual-head overhead removes any throughput gain in two independent seeds/shards.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-int2-draft-target-residual-logit-head-4bd4a68576ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
