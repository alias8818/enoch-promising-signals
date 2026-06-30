# Hierarchical chunked attention for 8k CPU context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-chunked-attention-for-8k-cpu-context-fd87fe9a65e1`
Run ID: `hierarchical-chunked-attention-for-8k-cpu-context-fd87fe9a65e1-20260528T023621088964+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c8ad9af5b056

## What looked useful

The tested hierarchy reached 8192 tokens cheaply on CPU and measured a 48.1x speedup over dense attention at chunk size 256, but it had 4.87 relative L2 error versus dense and failed a synthetic long-range retrieval probe where dense cosine was 1.0 and hierarchical cosine was -0.068. A chunk-size sweep from 16 to 512 did not fix retrieval; the best 8192-token cosine was 0.184.

## Boundaries and scale limits

No Transformer training, language-model perplexity, causal masking, multi-head KV-cache serving, learned summaries, or GPT-2-small-class baseline was tested. The result should not be read as a full rejection of all hierarchical chunked attention designs.

## Claim scope

A NumPy CPU probe of non-causal dense attention versus a simple hierarchical chunked approximation with exact local chunks and one mean key/value summary per chunk, tested up to 8192 tokens with d_model=64 and d_value=64.

## Why it stopped

Proxy/local early falsification of the simple mean-summary hierarchical mechanism: speed is supported, but dense-like behavior and long-range retrieval are not. Full validation would require learned-summary and trained-model evidence.

## Recommended next action

Stop this run as a no-paper useful signal; if pursued, test learned or routed summaries against the same 8k CPU retrieval and approximation thresholds before any model-training scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Routed summaries for 8k CPU hierarchical attention
- Success threshold: At n=8192, achieve at least 10x measured CPU speedup over dense attention, long-range retrieval cosine >= 0.85, and random-output relative L2 < 1.0, or provide a direct trained-task result showing these proxy metrics are not predictive.
- Stop condition: Stop if routed summaries cannot exceed retrieval cosine 0.5 at n=8192 under at least 10x speedup, or if their runtime approaches dense attention.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-chunked-attention-for-8k-cpu-context-fd87fe9a65e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
