# Anchor-Conditioned Draft Model Reduces Decode Latency on Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-conditioned-draft-model-reduces-decode-latency-on-long-context-9cb749f1b8a3`
Run ID: `anchor-conditioned-draft-model-reduces-decode-latency-on-long-context-9cb749f1b8a3-20260628T120025822902+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c6936620b079

## What looked useful

Anchor conditioning raised draft acceptance from 6.2%-13.2% to 100% and reduced target verifier calls from 2208-2592 to 768 over 24 x 128-token decodes, producing 2.85x-3.62x measured wall-clock speedup versus the unanchored draft. A constant-anchor control removed the benefit, supporting the anchor-information mechanism.

## Boundaries and scale limits

No real pretrained LLM, no learned draft model, no learned anchor extractor, no natural language quality metric, and no production serving stack. Evidence is limited to a local toy/proxy mechanism probe.

## Claim scope

Synthetic long-context speculative decoding benchmark where an oracle anchor id controls deterministic continuation tokens and the target verifier uses a GPU attention-like long-context read.

## Why it stopped

Closed as no-paper useful signal: the proxy mechanism is supported, but the evidence is synthetic/oracle-anchor only and is not a full validation of learned long-context LLM decoding.

## Recommended next action

Run a bounded learned-draft follow-up on a real or semi-real long-context anchor retrieval task before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Anchor-Conditioned Draft on Long-Context Retrieval
- Success threshold: At least 1.5x wall-clock decode speedup over the unanchored learned draft at equal output quality and at least 20 percentage points higher acceptance on contexts of 4096 tokens or longer.
- Stop condition: Stop if the learned anchor-conditioned draft fails to improve acceptance by at least 10 percentage points over the unanchored draft after matched training budget and validated anchor extraction.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-conditioned-draft-model-reduces-decode-latency-on-long-context-9cb749f1b8a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
