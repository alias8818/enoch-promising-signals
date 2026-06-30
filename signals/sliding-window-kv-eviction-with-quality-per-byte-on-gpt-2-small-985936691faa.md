# Sliding-window KV eviction with quality-per-byte on GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `sliding-window-kv-eviction-with-quality-per-byte-on-gpt-2-small-985936691faa`
Run ID: `sliding-window-kv-eviction-with-quality-per-byte-on-gpt-2-small-985936691faa-20260628T062001961499+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/73774bf46032

## What looked useful

The simple online attention-salience quality-per-byte score was worse than sliding-window in the main run and all four ablations. Recency reserve narrowed the gap, suggesting recency rather than salience carried most of the useful signal.

## Boundaries and scale limits

CPU-only local run; 288 total measured tokens; compressed contexts were recomputed with original position ids rather than implemented as live Transformers past_key_values mutation; no large corpus, multi-seed, or serving benchmark.

## Claim scope

On a bounded GPT-2-small retained-context proxy with a small synthetic/local trace, the tested attention-received quality-per-byte policy underperformed a same-budget sliding-window policy on next-token NLL.

## Why it stopped

Proxy early falsification: the tested QPB policy lost to sliding-window on mean NLL across the main run and ablations; this is not full serving validation of every QPB variant.

## Recommended next action

Stop this policy line unless a stronger online byte-value score first beats sliding-window in the same bounded GPT-2-small proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live GPT-2-small KV cache eviction after bounded proxy win
- Success threshold: Proceed only if the new score improves mean NLL over sliding-window by at least 0.1 in the proxy across three seeds and does not regress under live-cache evaluation.
- Stop condition: Stop if the new score fails to beat sliding-window in the proxy across three seeds or if live-cache position handling cannot reproduce the proxy token ordering faithfully.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-kv-eviction-with-quality-per-byte-on-gpt-2-small-985936691faa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
