# Real CPU Decoder Test of Periodic Salience KV Compaction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-cpu-decoder-test-of-periodic-salience-kv-compaction-0cef4b36d0`
Run ID: `real-cpu-decoder-test-of-periodic-salience-kv-compaction-0cef4b36d0-20260608T141026314279+0000`

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

- Parent run decision: Home CPU Long-Context Inference via Selective KV Pruning: enoch://control-plane/projects/home-cpu-long-context-inference-via-selective-kv-pruning-91908f5ed964/runs/home-cpu-long-context-inference-via-selective-kv-pruning-91908f5ed964-20260608T043303522696+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4965522b9dfe

## What looked useful

Salience compaction can reduce mean cache length by 42-57% in a real CPU decoder while often preserving baseline greedy outputs, but its advantage over recency is mixed. At budget 16 it had lower baseline-token NLL than recency/random with equal 0.912 exact agreement; at budget 24 recency achieved exact agreement and slightly better NLL than salience.

## Boundaries and scale limits

Small model, short prompts, greedy decoding, 8 hand-written prompts, max 64 generated tokens, unbatched CPU inference, no long-context retrieval/copy benchmark, no larger GPT-2-small-class model, and no production latency or memory-bandwidth profiling.

## Claim scope

In a controlled CPU distilgpt2 greedy-decoding test over 8 prompts and 64 generated tokens, periodic attention-salience KV compaction physically shortened real past_key_values and remained mechanically viable. It beat random and recency on baseline-token NLL only at the hardest 16-token budget, but did not robustly beat a recency-only control at the 24-token budget.

## Why it stopped

No-paper useful signal: the direct CPU decoder mechanism works, but the evidence is mixed and not robustly better than a simple recency control.

## Recommended next action

Run a bounded deepen follow-up on longer-context copy/needle prompts where preserving non-recent salient tokens is necessary; stop if salience does not beat recency on both baseline-token NLL and exact retrieval accuracy at equal KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Long-Context Retrieval Stress Test for Salience KV Compaction
- Success threshold: At the same mean KV cache length, salience must beat recency by at least 10 percentage points exact retrieval accuracy or reduce baseline-token NLL by at least 0.10 while maintaining at least 40% cache-length reduction versus full KV.
- Stop condition: Stop as negative if salience fails to beat recency on both retrieval accuracy and baseline-token NLL across two KV budgets, or if compaction breaks exact baseline retrieval more often than recency.

## Evidence references

- Artifact root: `<local-path>/projects/real-cpu-decoder-test-of-periodic-salience-kv-compaction-0cef4b36d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
