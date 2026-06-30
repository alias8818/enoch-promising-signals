# Live LLM operator-memory replay with authority and recency conflicts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-llm-operator-memory-replay-with-authority-and-recency-57a350c9f9`
Run ID: `live-llm-operator-memory-replay-with-authority-and-recency-57a350c9f9-20260614T061342461458+0000`

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

- Parent run decision: Operator-Model Memory Probe for CPU Agent: enoch://control-plane/projects/operator-model-memory-probe-for-cpu-agent-94d098a70851/runs/operator-model-memory-probe-for-cpu-agent-94d098a70851-20260614T045811985347+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a505c71cd74a

## What looked useful

Controlled replay supports the memory-selector mechanism, but the local live LLM execution path is too slow when each prompt starts a fresh CPU llama.cpp process.

## Boundaries and scale limits

Small synthetic task set only; live LLM end-to-end behavior was not validated because per-prompt CPU llama.cpp Qwen2.5-0.5B Q8_0 invocations timed out on all 6 target-strategy prompts.

## Claim scope

In a 6-task synthetic replay set, authority-then-recency memory selection with explicit expiry handling selected the expected memory and deterministic action for all tasks, outperforming no-memory, recency-only, and flat keyword-recency baselines.

## Why it stopped

No-paper closure: useful deterministic mechanism signal, but live LLM validation timed out and the evidence is not publication-grade.

## Recommended next action

Run a bounded deepen test with a persistent model server or API so model load is amortized, then score all four strategies end-to-end on the same 6 tasks before expanding the task set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent-runner live LLM authority-recency replay matrix
- Success threshold: Target authority-then-recency live action accuracy >= 5/6 and at least 2 correct-action wins over both recency-only and flat keyword-recency on the same task set.
- Stop condition: Stop after the 24-prompt matrix completes, or earlier if persistent runner setup cannot produce one parsed action within 5 minutes.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-operator-memory-replay-with-authority-and-recency-57a350c9f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
