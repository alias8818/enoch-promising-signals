# Home Distributed QAT: Frozen Ultra-low-bit Bulk with Synced Residual

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `home-distributed-qat-frozen-ultra-low-bit-bulk-with-synced-residual-547f4f68f119`
Run ID: `home-distributed-qat-frozen-ultra-low-bit-bulk-with-synced-residual-547f4f68f119-20260620T070712243201+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a258cba71a72

## What looked useful

Across seeds 7, 13, and 23, best synced residuals improved accuracy over frozen bulk by +0.0632 at 1-bit and +0.1932 at 2-bit, and beat unsynced local residuals by +0.0379 and +0.0304 respectively. Residual trainable parameters were 4.0% to 16.1% of bulk parameters with tiny per-sync payloads in the toy model.

## Boundaries and scale limits

Evidence is limited to a small in-process synthetic MLP. It does not validate GPT-2-small-class or larger transformers, real home-network communication, straggler/dropout behavior, true QAT updates to the frozen bulk, or full language-model perplexity/task quality.

## Claim scope

On a synthetic teacher MLP with five simulated non-IID clients, a frozen 1-bit or 2-bit quantized bulk can recover useful accuracy by training and periodically synchronizing low-rank residual adapters; synced residuals consistently beat frozen-only and unsynced local-adapter controls across three seeds.

## Why it stopped

No-paper useful signal: the local proxy supports the mechanism, but it is synthetic and in-process rather than direct language-model or real distributed evidence.

## Recommended next action

Run a bounded compact-transformer or GPT-2-small-class replication with the same frozen-low-bit, synced-residual, unsynced-residual, and full-fine-tune controls before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compact Transformer Frozen Low-bit Bulk with Synced Residual
- Success threshold: Synced residual improves held-out perplexity or task accuracy over frozen low-bit bulk and unsynced residual controls in at least two of three seeds while using no more than 20% residual trainable parameters.
- Stop condition: Stop if synced residual fails to beat unsynced residual or frozen-only controls on the compact transformer after the planned seeds, or if the run exceeds the local resource budget without intermediate evidence.

## Evidence references

- Artifact root: `<local-path>/projects/home-distributed-qat-frozen-ultra-low-bit-bulk-with-synced-residual-547f4f68f119`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
