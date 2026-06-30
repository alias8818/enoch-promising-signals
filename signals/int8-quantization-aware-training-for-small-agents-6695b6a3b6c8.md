# INT8 Quantization-Aware Training for Small Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-quantization-aware-training-for-small-agents-6695b6a3b6c8`
Run ID: `int8-quantization-aware-training-for-small-agents-6695b6a3b6c8-20260608T201235165426+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/43da9b60f994

## What looked useful

For very small policy networks, PTQ should be the first baseline. In this local test PTQ stayed within 0.2-1.2 percentage points of FP32 in the longer run, while QAT lost 2.6-12.9 points and INT8 CPU inference was slower than FP32.

## Boundaries and scale limits

Synthetic supervised policy proxy only; not online RL, not language-agent behavior, not GPT-2-small-class training, and not a production deployment benchmark. QAT schedule was standard and lightly tuned only by extending steps to 2100.

## Claim scope

On a synthetic compact key-door-goal policy imitation task with MLP widths 8/16/32 on NVIDIA GB10 training and aarch64 qnnpack INT8 CPU inference, post-training INT8 quantization preserved accuracy better than the tested PyTorch eager QAT recipe; INT8 was not faster for these tiny models and was only smaller at width 32.

## Why it stopped

No paper-ready positive result; this is a bounded proxy/useful-signal result showing PTQ dominates the tested QAT recipe for tiny synthetic policies.

## Recommended next action

Run a bounded real-agent follow-up on MiniGrid or CartPole-style policies with fused modules and a tuned QAT schedule; stop if PTQ remains within 1 percentage point of FP32 and QAT does not beat PTQ on accuracy plus footprint/latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent PTQ-vs-QAT Validation for Tiny Policies
- Success threshold: QAT INT8 must match FP32 within 1 percentage point, beat PTQ by at least 1 percentage point when PTQ degrades, and show a footprint or latency benefit on the target deployment path.
- Stop condition: Stop after three seeds if PTQ remains within 1 percentage point of FP32 or if QAT remains slower/larger without a task-metric advantage.

## Evidence references

- Artifact root: `<local-path>/projects/int8-quantization-aware-training-for-small-agents-6695b6a3b6c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
