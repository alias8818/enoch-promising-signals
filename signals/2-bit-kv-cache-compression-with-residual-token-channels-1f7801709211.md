# 2-bit KV-Cache Compression with Residual Token Channels

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `2-bit-kv-cache-compression-with-residual-token-channels-1f7801709211`
Run ID: `2-bit-kv-cache-compression-with-residual-token-channels-1f7801709211-20260629T141148882350+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/66965a9ddd71

## What looked useful

Best strategy, error-selected 6.25% residual channels for both K and V, reduced mean relative output MSE by 8.34% versus pure 2-bit while increasing indexed storage from 2.0 to 3.375 bits per KV entry. This misses the 25% predeclared useful-signal threshold; heavy-tail activations improved only 7.45%.

## Boundaries and scale limits

No real model perplexity, downstream accuracy, decode latency, paged-cache implementation, learned residual-mask predictor, or 7B+/serving-scale validation was run. Maximum synthetic tensor shape was heads=4, sequence length=512, dimension=64 over 45 cases and 315 strategy rows.

## Claim scope

Bounded synthetic attention probe over transformer-shaped Q/K/V tensors with 2-bit per-token symmetric K/V quantization and fixed per-token residual channel restoration. Evidence supports that residual channels improve fidelity slightly, but not enough to meet the predeclared threshold or justify paper-positive claims.

## Why it stopped

Early bounded proxy negative: residual token channels helped monotonically, but the best tested setting produced too little fidelity gain for its storage overhead and did not meet the predeclared success threshold.

## Recommended next action

Stop this simple residual-channel mechanism as no-paper evidence; only revisit if a new selector or metadata-free encoding can target heavy-tail errors with at least 25% attention-output MSE reduction under the same synthetic protocol before model-level testing.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-compression-with-residual-token-channels-1f7801709211`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
