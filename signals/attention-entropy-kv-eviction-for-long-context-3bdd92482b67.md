# Attention-Entropy KV Eviction for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `attention-entropy-kv-eviction-for-long-context-3bdd92482b67`
Run ID: `attention-entropy-kv-eviction-for-long-context-3bdd92482b67-20260629T050757146883+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/95600b59db12

## What looked useful

Entropy confidence can filter diffuse distractor observations, improving mixed-distractor relative output MSE at budgets 128 and 256, but across all seed/regime/budget comparisons it lost to plain heavy-hitter more often than it won on relative output MSE (128 wins, 150 losses, 42 ties) and retained future attention mass (121 wins, 157 losses, 42 ties).

## Boundaries and scale limits

No real transformer inference, LongBench/RULER evaluation, multi-layer cache interaction, or latency/memory bandwidth measurement was run. The result is a controlled proxy over context=4096 traces, 20 seeds, 4 regimes, 4 budgets, and 4 policies.

## Claim scope

Synthetic long-context attention/value traces show that query-level attention entropy weighting is not a robust replacement for plain heavy-hitter KV eviction. It helps tight-budget mixed-distractor traces but is neutral on clean sparse retrieval and harmful when diffuse attention is future-relevant or sharp observations are decoys.

## Why it stopped

Proxy evidence is sufficient to reject a blanket entropy-weighted KV eviction claim as no-paper evidence; full validation would require real model traces and task metrics.

## Recommended next action

Run a bounded real-model trace replay on GPT-2-small-class or small Llama/Qwen attention dumps for LongBench/RULER/needle tasks, comparing equal-budget heavy-hitter and entropy-weighted variants before considering any implementation-level KV cache integration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay entropy-weighted KV eviction on real model attention traces
- Success threshold: Entropy-weighted policy must improve task or trace-retention metrics by at least 5% relative over heavy-hitter at one or more tight budgets without more than 1% degradation on diffuse-relevant/control tasks.
- Stop condition: Stop if entropy-weighted scoring does not beat heavy-hitter on real traces at tight budgets or if gains are confined to synthetic-like cases without task-level improvement.

## Evidence references

- Artifact root: `<local-path>/projects/attention-entropy-kv-eviction-for-long-context-3bdd92482b67`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
